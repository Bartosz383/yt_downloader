from tkinter import filedialog, messagebox
from pytube import YouTube
from tkinter import *
from pytube import Playlist
import os
import sys


def WidgetsOneFile(root, videoLink, downloadPath, varCheckbox, clicked, resOptions):
    ytLink = Label(root, text="YouTube URL: ", width=13, bg="#33b249")
    ytLink.grid(row=0, column=0, padx=5, pady=5)

    root.ytLinkText = Entry(root, bg="#a1d99b", width=60, textvariable=videoLink)
    root.ytLinkText.grid(row=0, column=1, padx=5, pady=5)

    destinationLabel = Label(root, text="Destination: ", width=13, bg="#33b249")
    destinationLabel.grid(row=1, column=0, padx=5, pady=5)

    root.destinationText = Entry(root, width=60, bg="#a1d99b", textvariable=downloadPath)
    root.destinationText.grid(row=1, column=1, padx=5, pady=5)

    browseButton = Button(root, text="Browse", command=lambda: Browse(downloadPath), width=13, bg="#33b249")
    browseButton.grid(row=1, column=2, padx=5, pady=5)

    soundCheckbox = Checkbutton(root, text="Sound only", width=10, bg="#33b249", variable=varCheckbox, onvalue=True,
                                offvalue=False)
    soundCheckbox.deselect()
    soundCheckbox.grid(row=0, column=2, padx=5, pady=5)

    resolution = Label(root, text="Resolution: ", width=13, bg="#33b249")
    resolution.grid(row=2, column=0, padx=5, pady=5)

    resolutionMenu = OptionMenu(root, clicked, *resOptions)
    resolutionMenu.config(width=10, bg="#33b249")
    resolutionMenu["menu"].config(bg="#33b249")
    resolutionMenu.grid(row=3, column=0, padx=5, pady=5)

    downloadButton = Button(root, text="Download",
                            command=lambda: DownloadVideo(videoLink, downloadPath, varCheckbox, clicked), width=25,
                            bg="#33b249")
    downloadButton.grid(row=2, column=1, padx=5, pady=5)

    quitButton = Button(root, text="Quit", command=root.quit, width=25, bg="#33b249")
    quitButton.grid(row=3, column=1, padx=5, pady=5)


def WidgetsStart(master, varCheckbox, clicked):
    nextButton = Button(master, text="Next", command=lambda : MenuDownloadOneVideo(), width=25, bg="#33b249")
    nextButton.grid(row=0, column=1, padx=5, pady=5)

    multipleFileCheckbox = Checkbutton(master, text="Multiple File", width=20, bg="#33b249", variable=varCheckbox,
                                       onvalue=True, offvalue=False)
    multipleFileCheckbox.deselect()
    multipleFileCheckbox.grid(row=1, column=1, padx=5, pady=5)

    quitButton = Button(master, text="Quit", command=master.quit, width=25, bg="#33b249")
    quitButton.grid(row=3, column=1, padx=5, pady=5)


def Browse(downloadPath):
    downlandDirectory = filedialog.askdirectory(initialdir="Your Directory Path")
    downloadPath.set(downlandDirectory)


def DownloadVideo(videoLink, downloadPath, varCheckbox, clicked):
    url = videoLink.get()
    folder = downloadPath.get()
    onlyAudioSet = varCheckbox.get()
    resolutio = clicked.get()

    getVideo = YouTube(url)
    if onlyAudioSet == True:
        getStream = getVideo.streams.filter(only_audio=onlyAudioSet).first()
    elif onlyAudioSet == False:
        getStream = getVideo.streams.filter(only_audio=onlyAudioSet, res=resolutio).first()
    getStream.download(folder)

    messagebox.showinfo("Download Successful", "Your video is here " + getVideo.title + "\nVideo length: " + str(
        getVideo.length) + " seconds" + "\n" + folder)


def MenuDownloadMultipleVideo():
    path = "C:\\Users\\krusz\\Music\\"
    manyURLs = open("D:\Repozytoria i inne takie\yt_downloader\links.txt", 'r')
    count = 1

    for i in manyURLs:
        try:
            yt = YouTube(i)
        except:
            print("Error")

        yt.streams.filter(progressive=True, file_extension='mp4')
        hr = yt.streams.get_highest_resolution()

        try:
            hr.download(path)
            print(count, " Completed")
            count += 1
        except:
            print("Error")

    print("Completed")


def MenuDownloadOneVideo():
    root = Tk()
    root.title("YouTube Downloader")
    root.iconbitmap('YTdownloaderIcon.ico')
    root.configure(bg="black")

    resOptions = ["144p", "240p", "360p", "480p", "720p", "1080p"]

    videoLink = StringVar()
    downloadPath = StringVar()
    varCheckbox = BooleanVar()
    clicked = StringVar()
    clicked.set(resOptions[0])

    WidgetsOneFile(root, videoLink, downloadPath, varCheckbox, clicked, resOptions)

    root.mainloop()

def DownloadPlaylist():
    ytStreamAudio = '140'
    downloadPath = "C:\\Users\\krusz\Music\\Playlista"
    p = Playlist('https://www.youtube.com/playlist?list=PLY7Epj-qzAssCTx7i8D_qFt5IsprQ2gJK')
    #p = Playlist('https://www.youtube.com/playlist?list=PLY7Epj-qzAsvsXH600-wTqWpOue_dAgtv')

    print(f'Downloading: {p.title}')
    for video in p.videos:
        try:
            outFile = video.streams.get_by_itag(ytStreamAudio)
            outFile.download(output_path=downloadPath)
            print("file downloaded")
        except:
            print("Error")

    print("Download completed")

    for filename in os.listdir(downloadPath):
        try:
            infilename = os.path.join(downloadPath, filename)
            if not os.path.isfile(infilename): continue
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.mp4', '.mp3')
            output = os.rename(infilename, newname)
            print("file converted")
        except:
            print("Error")

    print("Conversion completed")

    count = 0
    # Iterate directory
    for path in os.listdir(downloadPath):
        # check if current path is a file
        if os.path.isfile(os.path.join(downloadPath, path)):
            count += 1
    print('File count:', count)


def main():
    master = Tk()
    # master.geometry("300x300")
    master.title("YouTube Downloader")
    master.iconbitmap('YTdownloaderIcon.ico')
    master.configure(bg="black")

    varCheckbox = BooleanVar()
    clicked = StringVar()

    WidgetsStart(master, varCheckbox, clicked)

    master.mainloop()


if __name__ == "__main__":
    # main()
    # MenuDownloadOneVideo()
    # DownloadMultipleVideo()
    # master()
    # DownloadPlaylist()
