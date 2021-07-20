from pytube import YouTube
import tkinter as tk
import tkinter.filedialog
window = tk.Tk()


#Author Dev_sniper
#©Dev_Sniper 2021


def downloadVideo(ys, frm_frame, yTitle):
    if ys != "":
        lbl_dwnld = tk.Label(text="Downloading")
        lbl_dwnld.grid(row=7, column=0, rowspan=2)
        ys.download(tkinter.filedialog.asksaveasfilename(title="Datei speichern", defaultextension=".mp4", filetypes=(("mp4 Datei", "*.mp4"),("Alle Dateitypen", "*.*")), initialfile=yTitle))
        lbl_dwnld.grid_forget()
        frm_frame.grid_forget()
        startMenu()
    else:
        print("no ys defined")

def downloadButton(ys, frm_frame, yTitle):
    btn_downloadButton = tk.Button(master=frm_frame, text="Download", command= lambda: downloadVideo(ys, frm_frame, yTitle))
    btn_downloadButton.grid(row=6, column=0)

def downloadMenu(yTitle, yViews, rlength, rseconds, yRating, yFileSize, yFileSizeApprox, ys):
    frm_frame = tk.Frame()
    frm_frame.grid(row=0, column=0)
    lbl_yttitle = tk.Label(master=frm_frame, text=f"""Titel: {yTitle}""")
    lbl_yttitle.grid(row=0, column=0)
    lbl_views = tk.Label(master=frm_frame, text=f"""Views: {yViews}""""")
    lbl_views.grid(row=1, column=0)
    lbl_length = tk.Label(master=frm_frame, text=f"""Länge: {str(rlength).replace(".0", "")}min {rseconds}s""")
    lbl_length.grid(row=2, column=0)
    lbl_rating = tk.Label(master=frm_frame, text=f"""Bewertung: {round(yRating * 20, 2)}%""")
    lbl_rating.grid(row=3, column=0)
    lbl_filesize = tk.Label(master=frm_frame, text=f"""Dateigröße: {round(yFileSize / 1000000, 2)}MB""")
    lbl_filesize.grid(row=4, column=0)
    lbl_filesizeApprox = tk.Label(master=frm_frame, text=f"""Geschätzte Größe {round(yFileSizeApprox / 1000000, 2)}MB""")
    lbl_filesizeApprox.grid(row=5, column=0)
    downloadButton(ys, frm_frame, yTitle)

def checkLink(ent_link, lbl_link, btn_checkLink):
    if ent_link.get() != "":
        link = ent_link.get()
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        yTitle = yt.title
        yViews = yt.views
        yLength = yt.length
        yRating = yt.rating
        yFileSize = ys.filesize
        yFileSizeApprox = ys.filesize_approx
        rlength = round(yLength / 60, 0)
        rseconds = yLength - (rlength * 60)
        lbl_link.grid_forget()
        ent_link.grid_forget()
        btn_checkLink.grid_forget()
        ent_link.delete(0, tk.END)
        downloadMenu(yTitle, yViews, rlength, rseconds, yRating, yFileSize, yFileSizeApprox, ys)
    else:
        print("No link given")

def startMenu():
    window.title("YouTube Downloader - Dev")
    lbl_link = tk.Label(text="Geben Sie hier Ihren Link ein")
    lbl_link.grid(row=0, column=0)
    ent_link = tk.Entry()
    ent_link.grid(row=1, column=0)
    btn_close = tk.Button(text="Beenden", command= window.destroy)
    btn_close.grid(row=30, column=0)
    btn_checkLink = tk.Button(text="Link überprüfen")
    btn_checkLink.configure(command= lambda: checkLink(ent_link, lbl_link, btn_checkLink))
    btn_checkLink.grid(row=2, column=0)

startMenu()
window.mainloop()
