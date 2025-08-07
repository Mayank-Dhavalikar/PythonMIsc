import tkinter as tk
from tkinter import ttk
import win32gui
import time
import threading

# Store window titles and hwnds
open_windows = {}

def get_own_window_title():
    return "Open Apps"

def get_open_windows(own_title):
    global open_windows
    open_windows = {}

    def enum_callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).strip()
            class_name = win32gui.GetClassName(hwnd)

            if (
                title and
                not title.lower().startswith("wv_") and
                title != own_title and
                "text input application" not in title.lower() and
                class_name not in ["Progman", "Shell_TrayWnd"]
            ):
                open_windows[title] = hwnd

    win32gui.EnumWindows(enum_callback, None)
    return list(open_windows.keys())

def focus_window(title):
    hwnd = open_windows.get(title)
    if hwnd:
        try:
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f"Error focusing window: {e}")

def update_window_list():
    own_title = get_own_window_title()
    while True:
        windows = get_open_windows(own_title)
        update_ui(windows)
        time.sleep(5)

def update_ui(windows):
    def update():
        for widget in frame.winfo_children():
            widget.destroy()

        for title in windows:
            btn = ttk.Button(frame, text=title, command=lambda t=title: focus_window(t))
            btn.pack(fill='x', padx=5, pady=2)

    root.after(0, update)

# ==== Tkinter UI ====

root = tk.Tk()
own_window_title = get_own_window_title()
root.title(own_window_title)
root.geometry("200x600+0+0")
root.attributes('-topmost', True)

ttk.Label(root, text="Open Apps", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill='both', expand=True, padx=5)

# Background refresh thread
thread = threading.Thread(target=update_window_list, daemon=True)
thread.start()

root.mainloop()
