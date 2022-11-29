from pytube import YouTube, Playlist
from tkinter import colorchooser, filedialog
from tkinter import *  # support gui in python


def VideoDownload():
    link = Link_Entery.get()
    yout = YouTube(link)
    videos = yout.streams.filter()
    videos[2].download()
    convertstatuslabel.configure(
        text="--------------- Video Download completed --------------")


def AudioDownload():
    link = Link_Entery.get()
    global audios, vid
    yout = YouTube(link)
    audios = yout.streams.filter(only_audio=True)
    audios[2].download()
    convertstatuslabel.configure(
        text="--------------- Audio Download completed --------------")


def PlaylistDownload():
    link = Link_Entery.get()
    global audios, vid
    yout = Playlist(link)
    for video in yout.videos:
        video.streams.first().download()
    convertstatuslabel.configure(
        text="--------------- Playlist Download completed --------------")


def ThumbnilDownload():
    link = Link_Entery.get()
    yout = YouTube(link)
    x = yout.thumbnail_url
    with open("Thumbnil.txt", "w") as f:
        f.write(x)
    convertstatuslabel.configure(
        text="--------------- Thumbnil Link Download completed --------------")


root = Tk()  # tkinter short form tk
root.title("Youtube Downloader")  # title set at top
# root.iconbitmap("icon.ico")  # icon
root.geometry('755x555+400+150')  # set width,height,left,top
root.configure(bg='#8E1616')  # backgroun color
root.resizable(False, False)  # maximize screen (x,y)

heading = Label(root, text="YouTube Downloader", font=(
    "poppins", 40, "bold"), bg="white", padx=30, relief=RIDGE, border=11)
heading.place(x=90, y=25)

link_Label = Label(root, text="Enter Link :-", font=(
    "arial", 14, "bold"), relief=RIDGE, bg="white", padx=5, pady=5)
link_Label.place(x=100, y=200)


Link_Entery = Entry(root, font=('arial', 16, 'italic bold'), bg="yellow", justify="center", relief=RIDGE,
                    selectbackground="black", selectforeground="white")
Link_Entery.insert(END, "Paste your link here")
Link_Entery.place(x=250, y=200, width=450, height=35)

button1 = Button(root, text="Download Video", command=VideoDownload, border=5, font=(
    "arial", 14, "bold"),
    activebackground="blue", activeforeground="white", width=18)
button1.place(x=140, y=300)


button2 = Button(root, text="Download Audio", command=AudioDownload,
                 font=("arial", 14, "bold"), border=5,
                 activebackground="blue", activeforeground="white", width=18)
button2.place(x=440, y=300)


button3 = Button(root, text="Download Playlist", command=PlaylistDownload, font=(
    "arial", 14, "bold"),
    activebackground="blue", border=5, activeforeground="white", width=18)
button3.place(x=140, y=370)


button4 = Button(root, text="Download Thumbnil", command=ThumbnilDownload, font=(
    "arial", 14, "bold"),
    activebackground="blue", border=5, activeforeground="white", width=18)
button4.place(x=440, y=370)

convertstatuslabel = Label(root, text="", font=(
    "arial", 20, "bold"), bg="#8E1616")
convertstatuslabel.place(x=90, y=430)

root.mainloop()
