#!/usr/bin/python

import time, curses

def main(screen):
  screen.nodelay(True)
  y, x = 0, 0
  dy, dx = 0, 0
  while True:
    row, col = screen.getmaxyx()
    s = time.ctime()
    screen.addstr(y, x, s, curses.A_BOLD)
    screen.refresh()
    time.sleep(0.1)
    screen.addstr(y, x, s, curses.A_INVIS)
    if y == 0:
      dy = 1
    if y >= row - 1:
      dy = -1
    if x == 0:
      dx = 1
    if x + len(s) >= col - 1:
      dx = -1
    y += dy
    x += dx
    c = screen.getch()
    if c == ord('q'):
      break
    if c == curses.KEY_LEFT:
      dx = -1
    if c == curses.KEY_RIGHT:
      dx = 1
    if c == curses.KEY_UP:
      dy = -1
    if c == curses.KEY_DOWN:
      dy = 1
curses.wrapper(main)

