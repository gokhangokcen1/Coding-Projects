import yt_dlp

link = input("link: ")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("indirildi")
