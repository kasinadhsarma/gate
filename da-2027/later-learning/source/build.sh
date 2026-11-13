d=$1; shift
cd /home/claude/films/$d
for k in "$@"; do python3 ../mk.py . render $k > r_$k.log 2>&1; done
python3 ../mk.py . mix >/dev/null 2>&1
ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -c copy v.mp4 && ffmpeg -y -loglevel error -i v.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k -shortest out.mp4
