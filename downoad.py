from tkinter import *
from pytube import YouTube
from pytube import Playlist



root = Tk()
root.title('PY-DownLoader')

options = ['Playist' , 'Single Video']

def download_vid():
    link = path_field.get()

    if X.get() == options[1]:
        youtubeObject = YouTube(link).streams.get_highest_resolution()
        youtubeObject.download()
    else:
         p = Playlist(link)
         for i in p:
             youtubeObject = i.streams.get_highest_resolution()
             youtubeObject.download()
    
path_lab = Label(
    root,
    text="Path Here",
    font=("consolas",20,'bold'),
    padx = 10,
    pady=10,
    relief='groove',
    bg='red',
    fg='white'
)
path_lab.pack(expand=True,fill='both',padx=30,pady=5)


path_field = Entry(
    root,
    width=30,
    relief = SUNKEN,
    borderwidth=3,
    font=('Consolas',20,'bold')
)
path_field.pack(expand=True,padx=30)

X = StringVar()

options_frame = Frame(
    root,
    padx=10,
    pady=10,
)
options_frame.pack()


for i in range(2):
    Radiobutton(
        options_frame ,
        variable = X,
        value=options[i],
        text = options[i],  
        padx=20,
        pady=10,
        font=('consolas',15,'bold')
        
    ).grid(row = 0 , column = i ,padx=30)

download_btn = Button(
    root,
    text = 'Download',
    font=('consolas',20,'bold'),
    padx=10,
    pady=10,
    bg='green',
    fg='white',
    command = download_vid
)
download_btn.pack(expand=True , fill = 'both' , padx = 30 , pady = 10)


root.mainloop()
