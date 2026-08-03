<?php

declare(strict_types=1);

/**
 * chat.php
 *
 * Receives a JSON prompt from app.js, sends it securely to the
 * Gemini API, and returns the generated response as JSON.
 */

header('Content-Type: application/json; charset=utf-8');

require __DIR__ . '/config.php';


/**
 * Send a JSON response and stop script execution.
 *
 * @param array<string, mixed> $data
 */
function sendJsonResponse(array $data, int $statusCode = 200): never
{
    http_response_code($statusCode);

    echo json_encode(
        $data,
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
    );

    exit;
}


// Only POST requests are accepted.
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    sendJsonResponse(
        ['error' => 'Request method not allowed.'],
        405
    );
}


// Verify that PHP cURL is available.
if (!function_exists('curl_init')) {
    sendJsonResponse(
        ['error' => 'The PHP cURL extension is not available.'],
        500
    );
}


// Read and decode the JSON request.
$rawInput = file_get_contents('php://input');

if ($rawInput === false || trim($rawInput) === '') {
    sendJsonResponse(
        ['error' => 'The request body is empty.'],
        400
    );
}

$input = json_decode($rawInput, true);

if (!is_array($input)) {
    sendJsonResponse(
        ['error' => 'The request body contains invalid JSON.'],
        400
    );
}

$prompt = isset($input['prompt'])
    ? trim((string) $input['prompt'])
    : '';

if ($prompt === '') {
    sendJsonResponse(
        ['error' => 'Please provide a valid prompt.'],
        400
    );
}


// Verify the private Gemini API key.
if (
    !defined('GEMINI_API_KEY')
    || trim((string) GEMINI_API_KEY) === ''
    || GEMINI_API_KEY === 'YOUR_API_KEY_HERE'
) {
    sendJsonResponse(
        ['error' => 'The Gemini API key is not configured.'],
        500
    );
}


// Current Gemini model and REST endpoint.
$model = defined('GEMINI_MODEL')
    ? GEMINI_MODEL
    : 'gemini-3.5-flash';

$url = sprintf(
    'https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent',
    rawurlencode($model)
);


// Prepare the Gemini request body.
$requestBody = json_encode(
    [
        'contents' => [
            [
                'role' => 'user',
                'parts' => [
                    [
                        'text' => $prompt,
                    ],
                ],
            ],
        ],
    ],
    JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);

if ($requestBody === false) {
    sendJsonResponse(
        ['error' => 'The Gemini request could not be prepared.'],
        500
    );
}


// Send the request to Gemini.
$curl = curl_init($url);

if ($curl === false) {
    sendJsonResponse(
        ['error' => 'The connection to Gemini could not be initialized.'],
        500
    );
}

curl_setopt_array(
    $curl,
    [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'x-goog-api-key: ' . GEMINI_API_KEY,
        ],
        CURLOPT_POSTFIELDS => $requestBody,
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2,
    ]
);

$responseBody = curl_exec($curl);
$httpCode = (int) curl_getinfo($curl, CURLINFO_HTTP_CODE);
$curlError = curl_error($curl);

curl_close($curl);


// Handle connection failures.
if ($responseBody === false) {
    error_log('Gemini cURL error: ' . $curlError);

    sendJsonResponse(
        ['error' => 'The server could not connect to Gemini.'],
        502
    );
}


// Decode the Gemini response.
$responseData = json_decode($responseBody, true);

if (!is_array($responseData)) {
    error_log('Invalid Gemini response: ' . $responseBody);

    sendJsonResponse(
        ['error' => 'Gemini returned an invalid response.'],
        502
    );
}


// Handle API errors.
if ($httpCode < 200 || $httpCode >= 300) {
    $apiError = $responseData['error']['message']
        ?? 'Gemini rejected the request.';

    error_log(
        sprintf(
            'Gemini API error %d: %s',
            $httpCode,
            $apiError
        )
    );

    sendJsonResponse(
        [
            'error' => $apiError,
            'status' => $httpCode,
        ],
        502
    );
}


// Collect all readable text parts from Gemini.
$parts = $responseData['candidates'][0]['content']['parts'] ?? [];

$replyParts = [];

if (is_array($parts)) {
    foreach ($parts as $part) {
        if (
            is_array($part)
            && isset($part['text'])
            && trim((string) $part['text']) !== ''
        ) {
            $replyParts[] = trim((string) $part['text']);
        }
    }
}

$reply = trim(implode("\n", $replyParts));

if ($reply === '') {
    sendJsonResponse(
        ['error' => 'Gemini returned an empty response.'],
        502
    );
}


// Return the successful response to app.js.
sendJsonResponse(
    [
        'reply' => $reply,
        'model' => $model,
    ]
);