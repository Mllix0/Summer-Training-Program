# Task 3 — Voice-to-Voice AI Assistant

This task implements a complete **Voice-to-Voice AI Assistant** that receives spoken input, converts it into text, generates a response using a Large Language Model, and converts the generated response back into spoken audio.

The project was developed in three independent subtasks before combining them into one final integrated application.

## Task Requirements

The required workflow was:

1. Convert audio input into text
2. Generate a response using an LLM such as Cohere
3. Convert the generated response into audio
4. Upload the project files and document the complete development process on GitHub

## Final Workflow

```text
User Voice
    ↓
Microphone Recording
    ↓
Speech-to-Text
    ↓
Recognized Transcript
    ↓
LLM Processing
    ↓
Generated AI Response
    ↓
Text-to-Speech
    ↓
Spoken AI Response
```

## Project Development Approach

The project followed this development method:

```text
Build Independently
        ↓
Test Independently
        ↓
Improve Each Component
        ↓
Integrate the Components
        ↓
Test the Complete Pipeline
        ↓
Document the Project
```

Instead of building the entire system in one large Python file, each stage was first developed as an independent modular application.

After all three subtasks worked successfully, they were integrated into the final Voice-to-Voice AI Assistant.

## Completed Components

### Subtask 1 — Speech-to-Text

Converts microphone audio into recognized text using OpenAI Whisper.

Main operations:

- Records microphone input
- Saves the recording as a WAV file
- Loads the Whisper model
- Detects the spoken language
- Recognizes the spoken words
- Saves the recognized transcript
- Displays processing times and session information

[Open Subtask 1 — Speech-to-Text](Subtask-1-Speech-to-Text/README.md)

---

### Subtask 2 — LLM Processing

Sends text input to Cohere and receives an AI-generated response.

Main operations:

- Accepts text input
- Validates the message
- Connects securely to Cohere
- Sends the message to the Chat API
- Receives the generated response
- Displays and saves the response
- Measures response and runtime information

[Open Subtask 2 — LLM Processing](Subtask-2-LLM-Processing/README.md)

---

### Subtask 3 — Text-to-Speech

Converts text into spoken audio using the Windows text-to-speech engine.

Main operations:

- Accepts text input
- Initializes the Windows speech engine
- Selects an installed voice
- Generates a WAV audio file
- Plays the generated speech
- Measures synthesis and playback times

[Open Subtask 3 — Text-to-Speech](Subtask-3-Text-to-Speech/README.md)

---

### Final Voice-to-Voice AI Assistant

Integrates all three subtasks into one complete application.

Main operations:

- Records a spoken question
- Converts speech into text
- Sends the transcript to Cohere
- Receives an AI-generated response
- Converts the response into speech
- Plays the spoken answer
- Saves all generated files
- Displays a complete session summary

[Open the Final Voice-to-Voice AI Assistant](Final-Voice-Assistant/README.md)

## Task Structure

```text
Task-3-Voice-to-Voice-AI-Assistant
│
├── README.md
│
├── Subtask-1-Speech-to-Text
│   ├── README.md
│   ├── source-code
│   ├── files
│   └── screenshots
│
├── Subtask-2-LLM-Processing
│   ├── README.md
│   ├── source-code
│   ├── files
│   └── screenshots
│
├── Subtask-3-Text-to-Speech
│   ├── README.md
│   ├── source-code
│   ├── files
│   └── screenshots
│
└── Final-Voice-Assistant
    ├── README.md
    ├── source-code
    ├── files
    └── screenshots
```

Each project section contains:

```text
README.md
```

Explains the objective, architecture, development process, installation, usage, results, challenges, and lessons learned.

```text
source-code/
```

Contains the modular Python source files and dependency configuration.

```text
files/
```

Contains safe example recordings, transcripts, responses, or generated audio files.

```text
screenshots/
```

Contains visual evidence of the application workflow and results.

## Technologies Used

- Python 3.11
- OpenAI Whisper
- Cohere Chat API
- Cohere Python SDK
- pyttsx3
- Windows SAPI5
- Windows `winsound`
- SoundDevice
- SciPy
- PyTorch
- python-dotenv
- FFmpeg
- Visual Studio Code
- GitHub

## System Architecture

The completed system contains four major processing stages:

```text
┌─────────────────────┐
│ Microphone Recording│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Speech-to-Text    │
│   OpenAI Whisper    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   LLM Processing    │
│       Cohere        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Text-to-Speech    │
│   Windows SAPI5     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Spoken AI Response  │
└─────────────────────┘
```

## Modular Design

The final application separates its responsibilities into dedicated modules:

```text
voice_assistant.py
        │
        ├── config.py
        ├── recorder.py
        ├── transcriber.py
        ├── llm_client.py
        ├── tts_engine.py
        └── utils.py
```

### `config.py`

Stores shared settings, environment variables, model names, recording settings, voice settings, and generated-file paths.

### `recorder.py`

Records microphone input and saves it as a WAV file.

### `transcriber.py`

Loads Whisper, recognizes speech, and detects the spoken language.

### `llm_client.py`

Connects to Cohere and generates an AI response from the recognized transcript.

### `tts_engine.py`

Converts the AI response into audio and plays the generated WAV file.

### `utils.py`

Handles terminal messages, countdowns, file saving, language-name conversion, and session summaries.

### `voice_assistant.py`

Acts as the controller that connects every processing stage.

## Generated Files

A successful final session creates:

```text
recording.wav
transcript.txt
response.txt
response_audio.wav
```

### `recording.wav`

Contains the original microphone input.

### `transcript.txt`

Contains the recognized text generated by Whisper.

### `response.txt`

Contains the response generated by Cohere.

### `response_audio.wav`

Contains the spoken version of the AI response.

Example files are available inside:

[Final Voice Assistant example files](Final-Voice-Assistant/files/)

## Security

The project uses a Cohere API key.

The real API key is stored locally in:

```text
.env
```

The `.env` file is excluded from GitHub through `.gitignore`.

A safe configuration template is included:

```text
.env.example
```

Example:

```env
COHERE_API_KEY=your_cohere_api_key_here
COHERE_MODEL=command-a-plus-05-2026
```

The real API key must never be uploaded to GitHub or displayed in screenshots.

## Development Stages

The task was completed through the following stages:

1. Create the Speech-to-Text development environment
2. Install Whisper, SoundDevice, SciPy, and FFmpeg
3. Record microphone audio
4. Save recordings as WAV files
5. Transcribe speech using Whisper
6. Detect the spoken language
7. Save recognized transcripts
8. Create the LLM Processing environment
9. Configure Cohere securely
10. Send text prompts to the Cohere Chat API
11. Receive and save AI responses
12. Create the Text-to-Speech environment
13. Test available Windows voices
14. Select and configure a speech voice
15. Generate and play response audio
16. Test all three subtasks independently
17. Create a clean final integration project
18. Combine the recording, transcription, LLM, and TTS modules
19. Add shared configuration and utilities
20. Add complete error handling
21. Add stage-by-stage processing measurements
22. Test silent input and cancellation
23. Test repeated sessions
24. Prepare safe example files
25. Capture screenshots
26. Document every component on GitHub

## Testing

Each subtask was tested independently before integration.

### Speech-to-Text Tests

- Microphone recording
- WAV-file generation
- Whisper model loading
- Speech recognition
- Language detection
- Empty or silent recordings
- Transcript saving
- User cancellation

### LLM Processing Tests

- Cohere authentication
- Valid API requests
- Empty input
- Generated-response extraction
- Response-file saving
- API error handling
- User cancellation

### Text-to-Speech Tests

- Speech-engine initialization
- Voice selection
- WAV-file generation
- Audio playback
- Previous-file replacement
- Empty input
- User cancellation

### Final Integration Tests

- Complete spoken-input-to-spoken-output workflow
- Silent recording
- Repeated sessions
- Generated-file replacement
- Fresh terminal execution
- API credential protection
- Controlled error handling

## Example Final Session

### Spoken Input

```text
Explain artificial intelligence in one sentence.
```

### Recognized Transcript

```text
Explain artificial intelligence in one sentence.
```

### Generated AI Response

```text
Artificial intelligence is a field of computer science that creates
systems capable of performing tasks that normally require human
intelligence, such as learning, reasoning, and problem-solving.
```

The response was then converted into speech and played automatically.

## Challenges and Solutions

### Silent or unclear recordings

Whisper initially returned no recognizable speech when the microphone recording was silent or too quiet.

The solution included:

- Adding a countdown
- Displaying `Speak now!`
- Testing the generated WAV recording
- Speaking clearly during the recording period

### API key protection

The Cohere API key could not be placed directly inside the Python source code.

The solution used:

```text
.env
.env.example
.gitignore
```

This keeps private credentials local while documenting the required configuration.

### Duplicate module names

Each independent subtask originally contained its own `config.py` and `utils.py`.

Copying these files directly into one folder would create conflicts.

The final project was therefore built in a clean folder, and the necessary settings and functions were carefully combined into shared modules.

### Voice availability

Windows voice names and indexes may differ between computers.

The Text-to-Speech module checks whether the preferred voice exists and safely falls back to the first available voice.

### Maintaining clean architecture

The full workflow could have been implemented in one large file.

Instead, the application separates every responsibility into a dedicated module, making the project easier to understand, test, maintain, and expand.

## What I Learned

Through this task, I learned how to:

- Record microphone audio using Python
- Work with WAV audio files
- Use OpenAI Whisper for speech recognition
- Detect spoken languages
- Connect Python applications to an LLM
- Use the Cohere Chat API
- Secure API keys using environment variables
- Convert text into spoken audio
- Work with Windows SAPI5 voices
- Generate and play WAV files
- Integrate independent software modules
- Design a shared configuration system
- Measure individual processing stages
- Handle errors across multiple services
- Use dataclasses for structured results
- Build a complete AI processing pipeline
- Test components independently before integration
- Prepare safe example files
- Create detailed technical documentation on GitHub

## Result

The final project successfully completes the required workflow:

```text
Audio Input
     ↓
Text
     ↓
LLM Response
     ↓
Audio Output
```

The assistant can receive a spoken question and respond with a generated spoken answer.

## Future Improvements

Possible improvements include:

- Continuous conversation mode
- Conversation history
- Reusing the loaded Whisper model
- Streaming speech recognition
- Streaming LLM responses
- Voice activity detection
- Automatic silence detection
- Push-to-talk controls
- Graphical user interface
- Arabic speech and voice support
- Adjustable recording duration
- Cloud-based natural voices
- Automatic microphone selection
- GPU-based Whisper processing
- Packaging the project as a Windows application

## Project Navigation

- [Subtask 1 — Speech-to-Text](Subtask-1-Speech-to-Text/README.md)
- [Subtask 2 — LLM Processing](Subtask-2-LLM-Processing/README.md)
- [Subtask 3 — Text-to-Speech](Subtask-3-Text-to-Speech/README.md)
- [Final Voice-to-Voice AI Assistant](Final-Voice-Assistant/README.md)
- [Back to AI Track](../README.md)
