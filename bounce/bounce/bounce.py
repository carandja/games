"""
Demo bouncing ball
"""
import curses
import time
import threading
import random

class Ball(threading.Thread):
    def __init__(self, win):
        threading.Thread.__init__(self)
        self.win = win
        self.height, self.width = win.getmaxyx()
        self.goon = True

    def quit(self):
        self.goon = False

    def run(self):
        posx = random.randint(0, self.width)
        posy = random.randint(0, self.height)
        diry = 1
        dirx = 1
        while self.goon:
            self.win.addch(posy, posx, ' ')
            if posx < 1:
                dirx = 1
            elif posx == self.width - 1:
                dirx = -1
            if posy < 1:
                diry = 1
            elif posy == self.height - 1:
                diry = -1
            posy += diry
            posx += dirx
            #self.win.addstr(4,4,"[{}][{}]".format(posy, posx))
            self.win.addch(posy, posx, 'O')
            self.win.refresh()
            #win.getch()
            time.sleep(0.1)

def main(winmain):
    """main function"""
    height = 17 
    width = 49
    baty = height // 2
    batx = width // 2
    batc = '\u20de'
    curses.curs_set(False)
    win = curses.newwin(height, width)
    win.nodelay
    win.bkgd('-')
    key = 0
    win.addch(baty, batx, batc)
    count = 0
    ball1 = Ball(win)
    ball1.start()
    ball2 = Ball(win)
    ball2.start()
    while key != 27:
        key = win.getch()
        time.sleep(0.1)
    ball1.quit()
    ball1.join()
    ball2.quit()
    ball2.join()

curses.wrapper(main)
