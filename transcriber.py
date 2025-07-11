import re
import os
import subprocess
import whisper
import yt_dlp
import json

def download_video(url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if not filename.endswith('.mp4'):
            base = os.path.splitext(filename)[0]
            filename = f"{base}.mp4"
        return filename

def transcribe_video(video_path, model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(video_path)
    return result["text"]

def pipeline(url):
    try:
        print("Downloading video...")
        video_path = download_video(url)
        print(f"Video downloaded to {video_path}")

        print("Transcribing video...")
        transcript = transcribe_video(video_path).strip()
        print("Transcription complete.")

        os.remove(video_path)
        print(f"Deleted {video_path}")

        return transcript
    
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return ""

def extract_links(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regular expression to match video URLs
    pattern = r'https?://[^\s)>\]}]+|www\.[^\s)>\]}]+'
    links = re.findall(pattern, content)
    return links

def update_script_in_json(json_file, link, script_text):
    with open(json_file, "r") as f:
        data = json.load(f)

    updated = False
    for entry in data:
        if entry.get("link") == link:
            entry["script"] = script_text
            updated = True
            break

    if updated:
        with open(json_file, "w") as f:
            json.dump(data, f, indent=2)
    else:
        print(f"⚠️ Link not found in JSON: {link}")

file_path = 'video_links.txt'
links = extract_links(file_path)
    
for link in links:
    transcript = pipeline(link)

    if transcript == "":
        print("⚠️ Skipped.")
        continue

    print(transcript)
    # update_script_in_json("example.json", link, transcript)