"""
    This is a simple class to test pads
"""
import curses
from curses import newpad

def main(winmain):
    """test pads"""
    height = 5
    width = 10
    posy = 3
    posx = 8
    win = newpad(height, width)
    win.bkgd('/')
    win.refresh(0, 0, posy, posx, posy + height, posx + width)
    winmain.getch()
    for line in range(height):
        win.insstr(line, 0, "0123456789")
    win.refresh(0, 0, posy, posx, posy + height, posx + width)
    winmain.getch()
curses.wrapper(main)
