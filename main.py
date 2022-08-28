from tkinter import filedialog, messagebox

from pytube import YouTube
from tkinter import *

def Widgets():
    ytLink = Label(root, text="YouTube URL: ", bg="#33b249")
    ytLink.grid(row=0, column=0, padx=5, pady=5)

    root.ytLinkText = Entry(root, width=60, bg="#a1d99b", textvariable=videoLink)
    root.ytLinkText.grid(row=0, column=1, padx=5, pady=5)

    destinationLabel = Label(root, text="Destination: ", bg="#33b249")
    destinationLabel.grid(row=1, column=0, padx=5, pady=5)

    root.destinationText = Entry(root, width=60, bg="#a1d99b", textvariable=downloadPath)
    root.destinationText.grid(row=1, column=1, padx=5, pady=5)

    browseButton = Button(root, text="Browse", command=Browse, width=10, bg="#33b249")
    browseButton.grid(row=1, column=2, padx=5, pady=5)

    downloadButton = Button(root, text="Download", command=DownloadVideo, width=25, bg="#33b249")
    downloadButton.grid(row=2, column=1, padx=5, pady=5)
    
    quitButton = Button(root, text="Quit", command=root.quit, width=25, bg="#33b249")
    quitButton.grid(row=3, column=1, padx=5, pady=5)

def Browse():
    downlandDirectory = filedialog.askdirectory(initialdir="Your Directory Path")

    downloadPath.set(downlandDirectory)

def DownloadVideo():

    url = videoLink.get()
    folder = downloadPath.get()

    getVideo = YouTube(url)
    getStream = getVideo.streams.first()
    getStream.download(folder)

    messagebox.showinfo("Download Successful", "Your video is here " + folder)

root = Tk()
root.title("YouTube Downloader")
#root.geometry("320x800")
#root.resizable(False, False)
root.configure(bg="black")

videoLink = StringVar()
downloadPath = StringVar()

Widgets()

root.mainloop()
