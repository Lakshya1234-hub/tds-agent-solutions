ffmpeg -f x11grab -r 30 -s 1920x1080 -i :0.0 -vcodec libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p -t 10 -c:a aac -b:a 128k output.mp4
