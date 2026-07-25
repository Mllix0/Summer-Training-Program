<?php
require_once "db.php";

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $id = $_POST["id"] ?? null;

    if ($id && is_numeric($id)) {
        $stmt = $pdo->prepare("SELECT status FROM records WHERE id = :id");
        $stmt->execute([":id" => $id]);
        $record = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($record) {
            $currentStatus = (int) $record["status"];
            $newStatus = $currentStatus === 0 ? 1 : 0;

            $updateStmt = $pdo->prepare("UPDATE records SET status = :status WHERE id = :id");
            $updateStmt->execute([
                ":status" => $newStatus,
                ":id" => $id
            ]);

            echo json_encode([
                "success" => true,
                "newStatus" => $newStatus
            ]);
            exit;
        }
    }
}

echo json_encode([
    "success" => false,
    "message" => "Invalid request"
]);
exit;
?>