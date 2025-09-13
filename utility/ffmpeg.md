### Cut a mp3 file for 1 minute
```sh
ffmpeg -i back.mp3 -t 00:01:00 -c copy back_cut.mp3

```
### Render in 4K by Manim
```sh
manim -pqh demo.py Demo --format=mp4 --resolution="3840,2160"
```

### Cut a mp4 file from 1 to 40 second
```sh
ffmpeg -i Demo.mp4 -ss 0 -t 40 -c copy output.mp4
```

### Fix encoding of video for youtube upload
```sh
ffmpeg -i trimmed.mp4 -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 128k -movflags +faststart fixed.mp4
```