# AI Karaoke Project

This project is a simple, console-based karaoke system. It fetches lyrics using the Genius API and downloads karaoke tracks from YouTube using `yt-dlp`.
It then displays real-time lyric highlighting in sync with the music.

---

## Features

- Automatic fetching of lyrics using Genius API
- Karaoke track download from YouTube via `yt-dlp`
- Time-synced lyrics based on song duration
- Real-time lyric highlighting (current line: bright green, others: yellow)
- Cross-platform compatible (Windows/Linux/Mac)

---

## AI Component

This project demonstrates a **basic level of AI integration** through:

- **Intelligent lyric parsing** using NLP-like filtering to clean up non-singing parts like `[Chorus]`, `[Verse]`, etc.
- **Synchronized timing logic**, where lyric display is mapped proportionally across the total audio duration.
- While no deep learning model is used, the real-time behaviour mimics human timing and enhances interactivity using simple automation and logic.

---

## Technologies Used

- Language: **Python**
- [Genius](https://genius.com/) API
- **yt-dlp**
- **mutagen** (for getting MP3 duration)
- **pygame** (for audio playback)
- Standard Libraries: `os`, `time`, `threading`

---

## Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/schak04/AI-Karaoke-Project
   cd AI-Karaoke-Project
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

1. Go to the `dist` folder and double-click `karaoke_project.exe`.
   *Alternatively, you can run the `run_karaoke.bat` file in the root directory.*
2. Enter the song name, and sit back as the system downloads lyrics and audio.
3. Sing along with the highlighted lyrics!

---

## Notes

- An internet connection is required for fetching lyrics and karaoke audio.
- Avoid using special characters in song names.
- If multiple songs have the same name, include the artist or band in your search.
Format: `<song> <artist/band>` instead of just `<song>`.
- Console must support ANSI escape codes (most modern terminals do).
- `build.bat` is for developers only. It can be used to rebuild `karaoke_project.exe` after making code changes.

---

## Conclusion

This project aims to deliver a smooth and enjoyable karaoke experience with synced lyrics and clean visual cues.
The base version is purely CLI-based, with future plans for the addition of a proper GUI and more features.

---
