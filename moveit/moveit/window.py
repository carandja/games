import curses
import random

def main(winmain):
    pady = 0
    padx = 0
    padw = 100
    padh = 100

    curses.curs_set(False)
    winmain.border()
    win = curses.newpad(padh, padw)

    def refresh_win():
        """refresh the window"""
        win.refresh(pady, padx, 1, 1, curses.LINES - 2, curses.COLS - 2)
        return winmain.getch()

    for l in range(padh):
        s = ''.join([random.choice('.      +-') for c in range(padw-1)])
        win.addstr(l, 0, s)
    refresh_win()
    refresh_win()
    key = win.getch()
    while key != 'x':
        pady += 1
        key = refresh_win()

def makeString(length, body, start=None, end=None):
    if start == None: start = body
    if end == None: end = start
    return start + body * (length-2) + end

curses.wrapper(main)
