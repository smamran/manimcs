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

### Intel VAAPI Linux GPU acceleration 4K@60fps encoding on Intel Xe graphics
```sh
export LIBVA_DRIVER_NAME=iHD
ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -i Demo.mp4 -vf 'format=nv12,hwupload' -c:v h264_vaapi -qp 23 -c:a aac -b:a 128k vaapi.mp4
```

### Intel iGPU (Quick Sync) Encoding
```sh
ffmpeg -i Demo.mp4 -c:v h264_qsv -preset fast -global_quality 23 -look_ahead 0 -pix_fmt nv12 -r 30 -g 30 -c:a aac -b:a 128k -movflags +faststart igpu.mp4
```

### Fix CPU Encoding
```sh
ffmpeg -i Demo.mp4 -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 128k -movflags +faststart cpu.mp4
```

### Reduce Resolution from 1080p (or Any) to 720p using intel QSV in windows
```sh
ffmpeg -i Demo.mp4 -c:v h264_qsv -b:v 2M -maxrate 2.5M -bufsize 4M -vf "scale=-1:720" -r 30 -g 30 -pix_fmt nv12 -c:a aac -b:a 128k -movflags +faststart Demo_720p_compressed.mp4
```
