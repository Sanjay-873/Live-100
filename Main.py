import os

# Start YouTube Livestream Bot
print("YouTube Livestream Bot Started!")

# Enter your YouTube live stream key here
stream_key = "29e8-em5j-pq0b-wa6g-59k6"

# Command to start live stream using FFmpeg
command = f"ffmpeg -re -i video.mp4 -c:v libx264 -preset fast -b:v 2500k -maxrate 2500k -bufsize 5000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/{stream_key}"

# Run the command
os.syst

