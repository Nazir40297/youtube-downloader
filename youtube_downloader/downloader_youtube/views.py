from django.shortcuts import render, redirect
import yt_dlp

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            # 'postprocessors': [{
            #     'key': 'FFmpegVideoConvertor',
            #     'preferredcodec': 'mp4',
            #     'preferredquality': '192'
            # }],
            'merge_output_format': 'mp4'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            message = "Download successful!"
        except Exception as e:
            message = f"An error occurred: {str(e)}"

        return render(request, 'downloader_youtube/youtube.html', {'message': message})

    return render(request, 'downloader_youtube/youtube.html')


