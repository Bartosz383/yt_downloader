from pytube import YouTube

print("Paste link here: ")
link = input()

yt = YouTube(link)
print("Title: ", yt.title, "\nView: ", yt.views)

print("Sound only? Yes - write whatever. False - click enter")
soundOnly = input()

print("Set resolution: 144p, 240p, 360p, 480p, 720p, 1080p")
resolution = input()

stream = yt.streams.filter(only_audio = soundOnly, res = resolution).first().download('/Users/krusz/OneDrive/Pulpit/MusicFromYT')
