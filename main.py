from pytube import YouTube
from sys import argv

print("Paste link here: ")
link = input()

yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)

stream = yt.streams.first()

stream.download('/Users/krusz/OneDrive/Pulpit/MusicFromYT')
