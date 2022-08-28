rom tkinter import filedialog, messagebox

from pytube import YouTube
from tkinter import *

def Widgets():
    ytLink = Label(root, text="YouTube URL: ", width=13, bg="#33b249")
    ytLink.grid(row=0, column=0, padx=5, pady=5)

    root.ytLinkText = Entry(root,bg="#a1d99b", width=60, textvariable=videoLink)
    root.ytLinkText.grid(row=0, column=1, padx=5, pady=5)

    destinationLabel = Label(root, text="Destination: ", width=13, bg="#33b249")
    destinationLabel.grid(row=1, column=0, padx=5, pady=5)

    root.destinationText = Entry(root, width=60, bg="#a1d99b", textvariable=downloadPath)
    root.destinationText.grid(row=1, column=1, padx=5, pady=5)

    browseButton = Button(root, text="Browse", command=Browse, width=13, bg="#33b249")
    browseButton.grid(row=1, column=2, padx=5, pady=5)

    soundCheckbox = Checkbutton(root, text="Sound only", command=AudioSet, width=10, bg="#33b249", variable=varCheckbox, onvalue=True, offvalue=False)
    soundCheckbox.deselect()
    soundCheckbox.grid(row=0, column=2, padx=5, pady=5)

    resolution = Label(root, text="Resolution: ", width=13, bg="#33b249")
    resolution.grid(row=2, column=0, padx=5, pady=5)

    resolutionMenu = OptionMenu(root, clicked, *resOptions)
    resolutionMenu.config(width=10, bg="#33b249")
    resolutionMenu["menu"].config(bg="#33b249")
    resolutionMenu.grid(row=3, column=0, padx=5, pady=5)

    downloadButton = Button(root, text="Download", command=DownloadVideo, width=25, bg="#33b249")
    downloadButton.grid(row=2, column=1, padx=5, pady=5)

    quitButton = Button(root, text="Quit", command=root.quit, width=25, bg="#33b249")
    quitButton.grid(row=3, column=1, padx=5, pady=5)

def AudioSet():
    audioCheck = Label(root, text=varCheckbox.get())
    audioCheck.grid(row=5, column=1, padx=5, pady=5)

def Browse():
    downlandDirectory = filedialog.askdirectory(initialdir="Your Directory Path")
    downloadPath.set(downlandDirectory)

def DownloadVideo():

    url = videoLink.get()
    folder = downloadPath.get()
    onlyAudioSet = varCheckbox.get()
    res = clicked.get()

    getVideo = YouTube(url)
    getStream = getVideo.streams.filter(res=res, only_audio=onlyAudioSet).first()
    getStream.download(folder)

    messagebox.showinfo("Download Successful", "Your video is here " + getVideo.title + folder)
    print(getVideo.streams)

root = Tk()
root.title("YouTube Downloader")
root.iconbitmap('C:/Users/krusz/PycharmProjects/pythonProject/YTdownloaderIcon.ico')
root.configure(bg="black")

videoLink = StringVar()
downloadPath = StringVar()
varCheckbox = BooleanVar()

resOptions = ["144p", "240p", "360p", "480p", "720p", "1080p"]

clicked = StringVar()
clicked.set(resOptions[0])

Widgets()

root.mainloop()
