"""
curses library test
"""
import curses

"""
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
"""

def main(winmain):
    """main function"""
    height = 17 
    width = 49
    curses.curs_set(False)
    win = curses.newwin(height, width)
    win.bkgd('-')
    win.addstr(3,3,"abcde")
    win.addstr(4,3,"fghij")
    win.getch()
    win.addch(3,5,'C')
    win.getch()
    win.insch(4,5,'H')
    win.getch()
    win.delch(4,4)
    win.getch()
    win.delch(3,1)
    win.getch()
    win.insch(3,1,'<')
    win.getch()
    win.addch(3,2,'>')
    win.getch()
curses.wrapper(main)
