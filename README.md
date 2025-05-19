# OpenCrosshairZoom
# A open source version of the crappy crosshair zoom widget for windows.

Created with python and is very lightweight.
way better than the $20 scam that CrosshairZoom is.
this is seperate from gamebar so it wont use that bloatware.

# DIRECTIONS:

pip install pillow pywin32 pygame

F2 centers the window on the mouse

F3 moves the window's top-left corner to the mouse

ESC exits the application

The window remains click-through and borderless

# To enable built in crosshair

change the following:

 pygame.draw.circle(self.screen, (R,G,B),
                                    (self.size//X, self.size//Y), RADIUS)

# To change update speed (FPS / FRAMERATE)

CHANGE self.clock.tick(60)

# COMPLETLY OPEN SOURCE!

# 100% FREE
