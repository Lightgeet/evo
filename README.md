# Desktop Virtual Assistant

A voice-controlled desktop assistant built with Python. It listens for spoken commands, responds with speech, and can open Google, tell the current time or day, and identify itself as Thor.

## Features

- Voice input through a microphone using `sounddevice`.
- Speech recognition in Indian English using Google's speech recognition service.
- Spoken responses using `pyttsx3`.
- Opens Google in your default web browser.
- Announces the current time and day of the week.
- Greets the user and responds to questions about its name.
- Continues listening until you say “bye”.

## Requirements

- Windows
- Python 3.10 or newer
- A working microphone
- Internet access for speech recognition

## Setup and run

1. Install Python and make sure the Python launcher (`py`) is available in PowerShell.
2. Clone the repository and move into its folder:

   ```powershell
   git clone https://github.com/Lightgeet/evo.git
   cd evo
   ```

3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell does not allow activating scripts, you can skip activation and use the virtual environment's Python executable in the next step.

4. Install the dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

   If you skipped activation, run:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Start the assistant:

   ```powershell
   python main.py
   ```

   If you skipped activation, run:

   ```powershell
   .\.venv\Scripts\python.exe main.py
   ```

When the assistant says “Listening”, speak a command. Allow microphone access for your terminal or Python in Windows **Settings > Privacy & security > Microphone** if prompted.

## Commands to try

- “Open Google”
- “Which day it is?”
- “Tell me the time”
- “Tell me your name”
- “Bye” to exit

Speech recognition uses Google's online service, so an internet connection is required. If no speech is recognized, check your microphone and Windows microphone permissions, then try speaking again.
