import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("300x150")

        pygame.mixer.init()

        self.is_playing = False
        self.current_song = ""

        # Create GUI components
        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)

    def load_song(self):
        self.current_song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.current_song:
            messagebox.showinfo("Loaded", f"Loaded song: {self.current_song}")

    def play_song(self):
        if self.current_song:
            if not self.is_playing:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()
                self.is_playing = True
                self.play_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)

    def stop_song(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
