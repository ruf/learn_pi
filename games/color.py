#!/usr/bin/python

import curses

def main(screen):
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, i)
  row, col = screen.getmaxyx()
  for i in range(233, 256):
    screen.addstr(0, 36 + (i - 233) * 2, '%2x' % i, curses.color_pair(i))
  for r in range(0, 6):
    for g in range(0, 6):
      for b in range(0, 6):
        i = r * 36 + g * 6 + b + 17
        screen.addstr(r + 2, g * 14 + b * 2, '%2x' % i, curses.color_pair(i))
  for i in range(0, 17):
    screen.addstr(0, i * 2, '%2x' % i, curses.color_pair(i))
  screen.getch()

print curses.wrapper(main)

