import tkinter as tk
from PIL import ImageGrab, ImageTk
import win32api
import win32con
import win32gui

class Magnifier:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("300x300+500+500")
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "white")
        
        self.canvas = tk.Canvas(self.root, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.locked_pos = None  # Stores the locked position
        self.root.update_idletasks()
        
        # Window styling
        hwnd = self.root.winfo_id()
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                             win32con.WS_EX_LAYERED | 
                             win32con.WS_EX_TRANSPARENT |
                             win32con.WS_EX_TOOLWINDOW)
        win32gui.SetLayeredWindowAttributes(hwnd, 0x00FFFFFF, 255, win32con.LWA_COLORKEY)

        # Bind keys
        self.root.bind("<F2>", self.lock_position)
        self.root.bind("<F3>", self.move_window)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        
        self.update()
        self.root.mainloop()

    def get_mouse_pos(self):
        return win32api.GetCursorPos()

    def lock_position(self, event=None):
        """Lock magnification to current mouse position"""
        self.locked_pos = self.get_mouse_pos()
        # Add red dot visual indicator
        self.canvas.create_oval(145, 145, 155, 155, fill='red', tags='indicator')

    def move_window(self, event=None):
        """Move window to current mouse position"""
        x, y = self.get_mouse_pos()
        self.root.geometry(f"300x300+{x}+{y}")

    def capture_screen(self, x, y):
        try:
            img = ImageGrab.grab(bbox=(
                max(0, x - 75),
                max(0, y - 75),
                min(win32api.GetSystemMetrics(0), x + 75),
                min(win32api.GetSystemMetrics(1), y + 75)
            )).resize((300, 300))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Capture error: {e}")
            return None

    def update(self):
        # Use locked position or current mouse position
        if self.locked_pos:
            x, y = self.locked_pos
        else:
            x, y = self.get_mouse_pos()
            
        img = self.capture_screen(x, y)
        if img:
            self.canvas.delete("all")
            # Recreate indicator if needed
            if self.locked_pos:
                self.canvas.create_oval(145, 145, 155, 155, fill='red')
            self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
            self.canvas.image = img
            
        self.root.after(10, self.update)

if __name__ == "__main__":
    Magnifier()
