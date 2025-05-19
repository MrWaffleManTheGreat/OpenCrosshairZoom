# OpenCrosshairZoom
# A open source version of the crappy crosshair zoom widget for windows.

![image](https://github.com/user-attachments/assets/96c1ba2f-d85e-44e4-af04-c0b57bc5bc32)


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

# To change zoom amount

bbox = (x-75, y-75, x+75, y+75)

it captures a 150×150 region around the cursor which is then resized to self.size × self.size (300×300 effectively giving a 2x zoom

# COMPLETLY OPEN SOURCE!

# 100% FREE


note in the image i use crossover for the crosshair
