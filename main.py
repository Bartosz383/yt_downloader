from pytube import YouTube

print("Paste link here: ")
link = input()

yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)

print("Sound only? True or False")
soundOnly = input()

stream = yt.streams.filter(only_audio=soundOnly).first().download('/Users/krusz/OneDrive/Pulpit/MusicFromYT')
