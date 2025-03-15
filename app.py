from flask import Flask, redirect, url_for, request, session, render_template, jsonify
import requests
import threading
import cv2
import os
import gdown
import random
import time
from ultralytics import YOLO
from urllib.parse import urlencode
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# MBTI Results
mbti_results = {
    "INTJ": "The Architect",
    "INFP": "The Mediator",
    "ENTJ": "The Commander",
    "ENFP": "The Campaigner",
    "ISTJ": "The Logistician",
    "ISFJ": "The Defender",
    "ESTJ": "The Executive",
    "ESFJ": "The Consul",
    "INTP": "The Logician",
    "INFJ": "The Advocate",
    "ENTP": "The Debater",
    "ENFJ": "The Protagonist",
    "ISFP": "The Adventurer",
    "ISTP": "The Virtuoso",
    "ESTP": "The Entrepreneur",
    "ESFP": "The Entertainer"
}

# Spotify API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

# Spotify URLs
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"


# Google Drive file ID of your YOLO model (you can get this from the shareable link)
MODEL_URL = "https://drive.google.com/uc?id=15T5uc8iMm5Fs8XQIHaRy8W6LYQrVErCQ"

# Function to download YOLO model weights from Google Drive
def download_model():
    output_path = "/opt/render/project/Yolo-Weights"  # Absolute path in Render's environment
    os.makedirs(output_path, exist_ok=True)  # Ensure the directory exists
    gdown.download(MODEL_URL, os.path.join(output_path, "best.pt"), quiet=False)

# Modify your YOLO initialization to download the model if not already present
if not os.path.exists("../Yolo-Weights"):
    print("Downloading YOLO model...")
    download_model()

# Initialize YOLO model
model = YOLO("/opt/render/project/Yolo-Weights/best.pt")
classNames = ["anger", "disgust", "fear", "happy", "neutral", "sad", "surprise"]


# Global variables
detected_emotion = None
emotion_songs = []
current_song_index = 0
is_paused = False

# Personality types
# PURPLE
@app.route('/intj')
def intj():
    return render_template('intj.html')

@app.route('/intp')
def intp():
    return render_template('intp.html')

@app.route('/entj')
def entj():
    return render_template('entj.html')

@app.route('/entp')
def entp():
    return render_template('entp.html')

# GREEN
@app.route('/infj')
def infj():
    return render_template('infj.html')

@app.route('/infp')
def infp():
    return render_template('infp.html')

@app.route('/enfj')
def enfj():
    return render_template('enfj.html')

@app.route('/enfp')
def enfp():
    return render_template('enfp.html')

# BLUE
@app.route('/istj')
def istj():
    return render_template('istj.html')

@app.route('/isfj')
def isfj():
    return render_template('isfj.html')

@app.route('/estj')
def estj():
    return render_template('estj.html')

@app.route('/esfj')
def esfj():
    return render_template('esfj.html')

# YELLOW
@app.route('/istp')
def istp():
    return render_template('istp.html')

@app.route('/isfp')
def isfp():
    return render_template('isfp.html')

@app.route('/estp')
def estp():
    return render_template('estp.html')

@app.route('/esfp')
def esfp():
    return render_template('esfp.html')

# Home, Quiz, Result Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/result')
def result():

    personality_type = request.args.get('personality_type', '')
    description = mbti_results.get(personality_type, "Unknown type")

    session.permanent = True  # Keep session persistent

    # Store MBTI type in session
    session['personality_type'] = personality_type  # Store in session
    session['description'] = description  # Store in session

    print("Stored in session:", session.get('personality_type'), session.get('description'))  # Debugging

    return render_template('result.html', personality_type=personality_type, description=description)


# Emotion detection function
def run_emotion_detection_on_image(image_path, access_token):
    global detected_emotion, emotion_songs  # Ensure we are using the global variable

    # Load the uploaded image
    img = cv2.imread(image_path)
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            detected_emotion = classNames[cls]

            # Fetch songs for the detected emotion
            fetched_songs = fetch_songs_for_emotion(detected_emotion, access_token)

            if fetched_songs:
                emotion_songs = fetched_songs  # Update the global emotion_songs list
                current_song_index = 0  # Start playing from the first song in the list
                play_song(emotion_songs[current_song_index], access_token)  # Play the first song
                return  # Once the first song is played, exit the loop

    print("No emotions detected or no songs returned.")





# Image upload route
@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'access_token' not in session:
        return redirect(url_for('login_spotify'))

    access_token = session['access_token']

    # Get the uploaded file
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)

        # Run emotion detection on the uploaded image
        threading.Thread(target=run_emotion_detection_on_image, args=(file_path, access_token)).start()

        # Return to the Spotify page (can update the UI with detected emotion later)
        return redirect(url_for('spotify'))

    return "Error: No file uploaded."


# Fetch songs based on emotion
def fetch_songs_for_emotion(emotion, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    # Emotion-to-search-term mapping
    emotion_to_search_term = {
        "anger": "energetic rock, adrenaline rush, power songs",
        "disgust": "experimental vibes, thought-provoking tunes, avant-garde music",
        "fear": "ambient calm, ethereal soundscapes, soothing instrumental",
        "happy": "uplifting pop, feel-good anthems, celebration hits",
        "neutral": "relaxing piano, easy listening, focus beats",
        "sad": "acoustic melancholy, heart-touching ballads, reflective tunes",
        "surprise": "dynamic beats, upbeat electronic, unexpected twists",
    }

    # Fallback to "chill vibes" if emotion is not mapped
    search_terms = emotion_to_search_term.get(emotion, "chill vibes")

    # Define search parameters
    params = {
        'q': search_terms,  # Use a comma-separated list of terms for broader results
        'type': 'track',
        'limit': 10  # Increase the limit for more songs
    }

    # Perform the search
    response = requests.get(f"{SPOTIFY_API_BASE_URL}/search", headers=headers, params=params)

    if response.status_code == 200:
        tracks = response.json().get('tracks', {}).get('items', [])
        print(f"Found {len(tracks)} tracks for emotion '{emotion}'")  # Debugging line
        if not tracks:
            print(f"No results found for search terms: {search_terms}")
            return []

        # Extract essential track details
        return [
            {
                'id': track['id'],
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'cover_url': track['album']['images'][0]['url'] if track['album']['images'] else ''
            }
            for track in tracks
        ]
    else:
        print(f"Error fetching songs for {emotion}: {response.status_code} - {response.text}")
        return []



# Function to play a song on the active device
def play_song(song, access_token):
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    # Get available devices
    devices_response = requests.get(f"{SPOTIFY_API_BASE_URL}/me/player/devices", headers=headers)
    devices = devices_response.json().get('devices', [])
    if not devices:
        print("No active devices found.")
        return

    device_id = devices[0]['id']  # Use the first available device
    track_uri = f"spotify:track:{song['id']}"
    play_url = f"{SPOTIFY_API_BASE_URL}/me/player/play?device_id={device_id}"

    # Activate the device
    activate_device_response = requests.put(
        f"{SPOTIFY_API_BASE_URL}/me/player",
        headers=headers,
        json={"device_ids": [device_id]}
    )
    print(f"Activate device response: {activate_device_response.status_code}")  # Debugging

    # Start playback
    start_playback_response = requests.put(play_url, headers=headers, json={"uris": [track_uri]})
    if start_playback_response.status_code == 204:
        print(f"Playing: {song['name']} by {song['artist']} on device {devices[0]['name']}")
    else:
        print(f"Failed to play song: {start_playback_response.text}")

# Spotify login route
@app.route('/login_spotify')
def login_spotify():
    if 'access_token' in session:
        return redirect(url_for('spotify'))

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-playback-state user-modify-playback-state user-read-private user-read-email streaming',
    }
    url = f"{SPOTIFY_AUTH_URL}?{urlencode(params)}"
    return redirect(url)

# Spotify OAuth callback
@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
        response = requests.post(SPOTIFY_TOKEN_URL, data=data)
        token_info = response.json()

        if 'access_token' in token_info:
            session['access_token'] = token_info['access_token']
            session['refresh_token'] = token_info.get('refresh_token')
            return redirect(url_for('spotify'))
    return "Error: Authorization failed."

# Spotify home route
@app.route('/spotify')
def spotify():
    if 'access_token' not in session:
        return redirect(url_for('login_spotify'))

    print("Retrieving from session:", session.get('personality_type'), session.get('description'))  # Debugging

    personality_type = session.get('personality_type', 'Not Available')
    description = session.get('description', 'No description available')

    return render_template('spotify.html', access_token=session['access_token'], personality_type=personality_type,
                           description=description)
@app.route('/reset_spotify')
def reset_spotify():
    session.pop('access_token', None)  # Remove access token from session
    session.pop('refresh_token', None)  # Remove refresh token as well (if exists)

    return redirect(url_for('login_spotify'))  # Redirect to Spotify login


# Start emotion detection
@app.route('/detect_emotion')
def detect_emotion():
    if 'access_token' not in session:
        return redirect(url_for('login_spotify'))

    access_token = session['access_token']
    threading.Thread(target=run_emotion_detection_on_image, args=(access_token,)).start()
    return redirect(url_for('spotify'))

# Control song playback
@app.route('/control/<action>')
def control(action):
    global current_song_index, is_paused

    if not emotion_songs:
        return jsonify({'error': 'No songs available to control'})

    access_token = session.get('access_token')
    if not access_token:
        return jsonify({'error': 'Access token is missing'})

    headers = {'Authorization': f'Bearer {access_token}'}

    if action == 'playpause':
        if is_paused:
            requests.put(f"{SPOTIFY_API_BASE_URL}/me/player/play", headers=headers)
            is_paused = False
        else:
            requests.put(f"{SPOTIFY_API_BASE_URL}/me/player/pause", headers=headers)
            is_paused = True
    elif action == 'next':
        current_song_index = (current_song_index + 1) % len(emotion_songs)
        play_song(emotion_songs[current_song_index], access_token)
    elif action == 'previous':
        current_song_index = (current_song_index - 1) % len(emotion_songs)
        play_song(emotion_songs[current_song_index], access_token)

    song = emotion_songs[current_song_index]
    return jsonify({
        'song': {
            'name': song['name'],
            'artist': song['artist'],
            'album': song['album'],
            'cover_url': song.get('cover_url', '')
        },
        'is_paused': is_paused
    })

@app.route('/get_detected_emotion')
def get_detected_emotion():
    return jsonify({'detected_emotion': detected_emotion})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default to port 8080 if PORT is not set
    app.run(debug=False, host='0.0.0.0', port=port)



