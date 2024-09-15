from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    yt_url = request.form['yt_url']
    
    try:
        yt = YouTube(yt_url)
        stream = yt.streams.get_highest_resolution()
        video_file = stream.download()

        return send_file(video_file, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
