from lyricsgenius import Genius
import yt_dlp
import os
import threading
import time
import pygame
from mutagen.mp3 import MP3

# === SETUP ===
GENIUS_API_TOKEN = "Ck5Q6uo_T8LYrAKw8l8e7i1jhqLox4l-9zrb1cd4oUvuWUkP_d2fPFv_hhwjv2m-"
genius = Genius(GENIUS_API_TOKEN)

# === USER INPUT ===
song_name = input("Enter the song name: ")

# === FETCH LYRICS ===
song = genius.search_song(song_name)
if song:
    print("\nLyrics found!\n")
    lyrics = song.lyrics
    lyrics_lines = lyrics.split('\n')

    # Clean up the lyrics:
    lyrics_lines = [
        line.strip() for line in lyrics_lines
        if line.strip() and not (line.strip().startswith('[') and line.strip().endswith(']'))
    ]
else:
    print("Lyrics not found.")
    exit()

# === DOWNLOAD AUDIO FROM YOUTUBE USING yt-dlp ===
print("Downloading audio from YouTube...")

def download_audio(search_query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': 'song.%(ext)s',
        'quiet': False,
        'default_search': 'ytsearch',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query + " karaoke"])

download_audio(song_name)
print("Audio downloaded!")

# === GET AUDIO DURATION ===
audio = MP3("song.mp3")
audio_duration = audio.info.length

# === COLOURED LYRICS DISPLAY FUNCTION ===
def display_lyrics(lyrics_lines, total_duration):
    print("\n🎤 Get ready to sing! 🎤")
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    time.sleep(1)  # Small buffer after countdown

    interval = total_duration / len(lyrics_lines)

    for idx, current_line in enumerate(lyrics_lines):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()  # Newline before first lyric

        for line_idx, line in enumerate(lyrics_lines):
            if line_idx == idx:
                print(f"\033[92m{line}\033[0m")  # Bright green
            else:
                print(f"\033[93m{line}\033[0m")  # Yellow

        time.sleep(interval)

print("Starting the karaoke session!")

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")

# Start music playback
pygame.mixer.music.play()

# Start lyrics display in parallel
lyrics_thread = threading.Thread(target=display_lyrics, args=(lyrics_lines, audio_duration))
lyrics_thread.start()

# Wait for music to finish
while pygame.mixer.music.get_busy():
    time.sleep(1)

lyrics_thread.join()

# === CLEANUP ===
pygame.mixer.quit()
os.remove("song.mp3")
print("Done!")

# === Exit ===
input("Press Enter to exit...")
