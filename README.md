
## 🔍 What is this?
This is a pipeline that takes a list of short video links (Instagram Reels, TikToks) and automatically:
1. Downloads the audio or video
2. Transcribes the speech into clean text
3. Outputs a structured JSON/CSV of links and scripts

## 🛠️ How It Works

1. 📄 Input: `video_links.txt` file with Instagram or TikTok links
2. 🎥 Download: The tool uses yt-dlp fetch the video/audio
3. 🗣️ Transcribe: Audio is sent to Whisper (speech-to-text engine)
4. 📤 Output: Clean script (e.g. JSON)

## 🚀 Quickstart
```bash
pip install -r requirements.txt
python transcribe.py
```