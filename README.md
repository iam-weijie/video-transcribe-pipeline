
> Extract scripts from Instagram/TikTok short videos and prep them for content analysis.

## 🔍 What is this?
`vidscribe` is a pipeline that takes a list of short video links (Instagram Reels, TikToks) and automatically:
1. Downloads the audio or video
2. Transcribes the speech into clean text
3. Outputs a structured JSON/CSV of links and scripts

This is the first step toward building LLM-powered content analysis tools (e.g. hook extraction, script generation, idea matching).

## 🛠️ How It Works

1. 📄 Input: A `.txt` file with Instagram or TikTok links
2. 🎥 Download: The tool uses yt-dlp or similar to fetch the video/audio
3. 🗣️ Transcribe: Audio is sent to a speech-to-text engine (e.g. Whisper)
4. 📤 Output: Clean script + metadata in JSON or CSV

## 🚀 Quickstart
```bash
pip install -r requirements.txt
python transcribe.py --input video_links.txt
```