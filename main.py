from pytube import YouTube
from sys import argv

#link = argv[1]
#yt = YouTube(link)

print("Paste link here: ")
link = input()

yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)

#print("Title: '", yt.title)

#print("View: ", yt.views)

stream = yt.streams.first()
#stream.download()

stream.download('/Users/krusz/OneDrive/Pulpit/MusicFromYT')
#yd.download('C:\Users\krusz\OneDrive\Pulpit\Nowy folder')