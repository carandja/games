"""
Interactive bouncing ball
Revsion from Yoga
"""
import curses
import time
import threading
import time

class Ball(threading.Thread):
    def __init__(self, win):
        threading.Thread.__init__(self)
        self.win = win
        self.height, self.width = win.getmaxyx()
        self.goon = True

    def quit(self):
        self.goon = False

    def run(self):
        posy = 3
        posx = 25 
        diry = 1
        dirx = 1
        while self.goon:
            self.win.delch(posy, posx)
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
    baty = height / 2
    batx = width / 2
    curses.curs_set(False)
    win = curses.newwin(height, width)
    win.nodelay
    win.bkgd('-')
    ball = Ball(win)
    ball.start()
    key = 0;
    while key != 27:
        key = win.getch()
        time.sleep(0.1)
    ball.quit()
    ball.join()

curses.wrapper(main)
