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

### Intel iGPU (Quick Sync) Encoding
```sh
ffmpeg -i Demo.mp4 -c:v h264_qsv -preset fast -global_quality 23 -look_ahead 0 -pix_fmt nv12 -r 30 -g 30 -c:a aac -b:a 128k -movflags +faststart igpu.mp4
```

### Fix CPU Encoding
```sh
ffmpeg -i Demo.mp4 -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 128k -movflags +faststart cpu.mp4
```
