import curses


def main(winmain):
    key = winmain.getch()
    while key != ord('x'):
        winmain.clear()
        winmain.addstr(5, 5, ">{}<".format(key))
        key = winmain.getch()

curses.wrapper(main)
