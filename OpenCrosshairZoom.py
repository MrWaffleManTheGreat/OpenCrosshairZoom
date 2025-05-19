import pygame
import sys
import win32api
import win32con
import win32gui
from PIL import ImageGrab
import pygame.transform

class PygameMagnifier:
    def __init__(self):
        pygame.init()
        self.size = 300
        self.screen = pygame.display.set_mode((self.size, self.size), 
                            pygame.NOFRAME | pygame.SRCALPHA)
        self.setup_window_properties()
        
        self.locked_pos = None
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Set initial window position
        self.window_pos = [500, 500]
        self.update_window_position()

    def setup_window_properties(self):
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                             win32con.WS_EX_LAYERED |
                             win32con.WS_EX_TRANSPARENT |
                             win32con.WS_EX_TOOLWINDOW)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def update_window_position(self):
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
                            self.window_pos[0], self.window_pos[1],
                            self.size, self.size, 0)

    def get_target_position(self):
        return self.locked_pos if self.locked_pos else win32api.GetCursorPos()

    def capture_area(self, pos):
        try:
            x, y = pos
            bbox = (x-75, y-75, x+75, y+75)
            img = ImageGrab.grab(bbox).resize((self.size, self.size))
            return pygame.image.fromstring(img.tobytes(), img.size, img.mode)
        except Exception as e:
            print(f"Capture error: {e}")
            return None

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F2:
                        self.locked_pos = win32api.GetCursorPos()
                    elif event.key == pygame.K_F3:
                        self.window_pos = list(win32api.GetCursorPos())
                        self.update_window_position()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False

            target_pos = self.get_target_position()
            captured = self.capture_area(target_pos)
            
            if captured:
                self.screen.blit(captured, (0, 0))
                if self.locked_pos:
                    pygame.draw.circle(self.screen, (255,0,0), 
                                    (self.size//0.001, self.size//0.001), 0.1)
                pygame.display.update()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    magnifier = PygameMagnifier()
    magnifier.run()