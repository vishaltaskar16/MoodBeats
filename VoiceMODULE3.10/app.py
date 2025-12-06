from flask import Flask, render_template, request, jsonify
import os
from predict import predict_emotion
import librosa
import soundfile as sf
import requests
import json

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# YouTube API Configuration
YOUTUBE_API_KEY = "AIzaSyCgGI7FoIgYlMqAnglKEHl1_ENKcfhcrFQ"  # Replace with your actual API key
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

def convert_to_wav(input_path, output_path):
    audio, sr = librosa.load(input_path)
    sf.write(output_path, audio, sr)

def get_youtube_videos(mood, content_type="song", max_results=10):
    """
    Fetch YouTube videos based on mood and content type
    """
    # Mood to search query mapping
    mood_queries = {
        "happy": {
            "song": ["happy music", "upbeat songs", "positive vibes music", "feel good songs"],
            "short": ["funny shorts", "happy moments", "comedy sketches", "dance challenges"]
        },
        "sad": {
            "song": ["sad songs", "emotional music", "melancholy songs", "heartbreak music"],
            "short": ["emotional stories", "sad poems", "rainy day vibes", "heartfelt moments"]
        },
        "angry": {
            "song": ["rock music", "heavy metal", "intense music", "powerful songs"],
            "short": ["intense workouts", "powerful moments", "action scenes", "motivational speeches"]
        },
        "neutral": {
            "song": ["chill music", "background music", "ambient sounds", "lo-fi beats"],
            "short": ["calming nature", "meditation guides", "relaxing scenes", "peaceful moments"]
        },
        "fearful": {
            "song": ["soothing music", "calm piano", "relaxing sounds", "peaceful melodies"],
            "short": ["comforting videos", "soothing nature", "calming scenes", "peaceful moments"]
        }
    }
    
    # Default queries if mood not found
    default_queries = {
        "song": ["music", "songs", "audio"],
        "short": ["shorts", "videos", "clips"]
    }
    
    queries = mood_queries.get(mood.lower(), default_queries).get(content_type, default_queries[content_type])
    
    videos = []
    for query in queries:
        if len(videos) >= max_results:
            break
            
        params = {
            'part': 'snippet',
            'q': f'{query} {content_type}',
            'type': 'video',
            'maxResults': min(10, max_results - len(videos)),
            'key': YOUTUBE_API_KEY,
            'videoDuration': 'short' if content_type == "short" else 'medium'
        }
        
        try:
            response = requests.get(YOUTUBE_API_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                for item in data.get('items', []):
                    video_data = {
                        'id': item['id']['videoId'],
                        'title': item['snippet']['title'],
                        'thumbnail': item['snippet']['thumbnails']['high']['url'],
                        'channel': item['snippet']['channelTitle'],
                        'description': item['snippet']['description']
                    }
                    videos.append(video_data)
        except Exception as e:
            print(f"Error fetching YouTube data: {e}")
    
    return videos[:max_results]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "audio" not in request.files:
        return "No file uploaded!"

    audio_file = request.files["audio"]

    ext = audio_file.filename.split(".")[-1]
    temp_input = os.path.join(UPLOAD_FOLDER, "input." + ext)
    temp_wav = os.path.join(UPLOAD_FOLDER, "converted.wav")

    audio_file.save(temp_input)

    try:
        convert_to_wav(temp_input, temp_wav)
    except:
        return "Error converting audio!"

    emotion, confidence = predict_emotion(temp_wav)

    return f"""
        <h2>🎵 Emotion Detection Result</h2>
        <p><b>Emotion:</b> {emotion}</p>
        <p><b>Confidence:</b> {confidence:.2f}</p>
        <a href='/'>Go Back</a>
    """

@app.route("/api/detect", methods=["POST"])
def api_detect():
    """
    API endpoint for emotion detection that returns JSON
    """
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded!"}), 400

    audio_file = request.files["audio"]

    ext = audio_file.filename.split(".")[-1]
    temp_input = os.path.join(UPLOAD_FOLDER, "input." + ext)
    temp_wav = os.path.join(UPLOAD_FOLDER, "converted.wav")

    audio_file.save(temp_input)

    try:
        convert_to_wav(temp_input, temp_wav)
    except Exception as e:
        return jsonify({"error": "Error converting audio!"}), 500

    emotion, confidence = predict_emotion(temp_wav)

    return jsonify({
        "emotion": emotion,
        "confidence": float(confidence)
    })

@app.route("/api/youtube/songs/<mood>")
def get_youtube_songs(mood):
    """
    API endpoint to get YouTube songs for a specific mood
    """
    songs = get_youtube_videos(mood, "song", 8)
    return jsonify({"songs": songs})

@app.route("/api/youtube/shorts/<mood>")
def get_youtube_shorts(mood):
    """
    API endpoint to get YouTube shorts for a specific mood
    """
    shorts = get_youtube_videos(mood, "short", 10)
    return jsonify({"shorts": shorts})

if __name__ == "__main__":
    app.run(debug=True)