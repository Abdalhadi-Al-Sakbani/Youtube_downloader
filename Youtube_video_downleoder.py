# from the tkinter library
import os
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, filedialog
from pytube import YouTube


def download_video():
    url = urlEntry.get()
    location = foldername.get()
    if url != "":
        try:
            yt = YouTube(url)
            stream = yt.streams.get_by_itag(22)
            # check for destination to save file
            destination = location if location != "" else r"C:\Users\abdsa\Downloads\Video"

            # download the file
            out_file = stream.download(output_path=destination)

            # save the file as .mp4
            base, ext = out_file.split('.')
            new_file = base + '.mp4'
            yt.register_on_complete_callback(lambda: rename_file(out_file, new_file))
            yt.register_on_complete_callback(show_complete)

        except Exception as e:
            show_error_message(str(e))
    else:
        show_error_message("Please provide a URL.")


# Function for opening the
# file explorer window

def browse_files():
    folder_path = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    foldername.set(folder_path)
    label_file_explorer.config(text=f"Folder Opened : {folder_path}")


def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        messagebox.showinfo("Download Complete", "Video downloaded successfully.")
    except Exception as e:
        show_error_message(str(e))


def show_error_message(message):
    messagebox.showerror("Error", message)


def show_complete():
    messagebox.showinfo("Download Complete", "Video downloaded successfully.")


is_dark_mode = False


def apply_theme(theme):
    window.config(bg=theme["bg"])
    label_title.config(bg=theme["bg"], fg=theme["fg"])
    label_file_explorer.config(bg=theme["label_bg"], fg=theme["label_fg"])
    urlEntry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    button_explore.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    submit_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    mode_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])


def apply_changes():
    global is_dark_mode

    if is_dark_mode:
        apply_theme(light_mode)
    else:
        apply_theme(dark_mode)

    is_dark_mode = not is_dark_mode


light_mode = {
    "bg": "#F3F3F3",
    "fg": "#21698f",
    "label_bg": "#F3F3F3",
    "label_fg": "#333333",
    "entry_bg": "#F3F3F3",
    "entry_fg": "black",
    "btn_bg": "#6ac2f7",
    "btn_fg": "#333333"
}

dark_mode = {
    "bg": "#333333",
    "fg": "#40b1ed",
    "label_bg": "#333333",
    "label_fg": "#FFFFFF",
    "entry_bg": "#d4d4d4",
    "entry_fg": "black",
    "btn_bg": "#007CBE",
    "btn_fg": "#FFFFFF"
}

# Create the root window
window = tk.Tk()

# Set window title
window.title('YouTube Downloader')

# Set custom fonts
title_font = tkfont.Font(family="Arial", size=20, weight="bold")
button_font = tkfont.Font(family="Arial", size=12)

# Set image content
image = tk.PhotoImage(file=r"B:\Programming\python\Youtube downloader\icons8-dark-mode-64 (Custom).png")

window.geometry("500x300")
window.config(background="#F3F3F3")  # Light gray background

label_title = tk.Label(window,
                       text="YouTube Downloader",
                       font=title_font,
                       fg="#21698f",
                       bg="#F3F3F3")

label_title.pack(pady=20)

urlEntry = tk.Entry(window,
                    bd=3,
                    font=button_font,
                    bg="#FFFFFF")  # White background

urlEntry.pack(pady=10)

foldername = tk.StringVar()
label_file_explorer = tk.Label(window,
                               text="Select Folder ",
                               font=button_font,
                               fg="#333333",
                               bg="#F3F3F3")  # Dark gray text on light gray background

label_file_explorer.pack()

button_explore = tk.Button(window,
                           text="Browse",
                           command=browse_files,
                           font=button_font,
                           fg="#333333",
                           bg="#6ac2f7")

button_explore.pack(pady=10)

submit_button = tk.Button(window,
                          text="Download",
                          command=download_video,
                          font=button_font,
                          fg="#333333",
                          bg="#6ac2f7")

submit_button.pack(pady=10)

mode_button = tk.Button(window,
                        command=apply_changes,
                        font=button_font,
                        fg="#333333",
                        bg="#6ac2f7",
                        image=image)

mode_button.place(relx=0.95, rely=0.16, anchor="s")

window.mainloop()
