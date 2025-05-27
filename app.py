from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'status': 'running',
        'message': 'DRM Uploader Bot is active',
        'creator': 'Tushar',
        'platform': 'Render'
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'drm-uploader-bot'
    })

@app.route('/status')
def bot_status():
    return jsonify({
        'bot_status': 'online',
        'platform': 'Render',
        'features': [
            'Video Download',
            'Text Processing', 
            'YouTube Playlist',
            'DRM Protection',
            'File Upload'
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
