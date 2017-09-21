#!/usr/bin/python

import time, random, curses

def main(screen):
  curses.curs_set(0)
  screen.nodelay(True)
  row, col = screen.getmaxyx()
  m = [] # [y, x, c]
  t = 1
  hit = miss = 0
  last = time.time()
  while miss < 10:
    for y, x, c in m:
      screen.addstr(y, x, c, curses.A_BOLD)
    screen.addstr(0, 0, '  Hit:%d  Miss:%d T:%.2f  ' % (hit, miss, t), curses.A_REVERSE)
    screen.refresh()
    time.sleep(0.05)
    k = screen.getch()
    if k == curses.KEY_UP:
      break
    n = []
    for y, x, c in m:
      screen.addstr(y, x, ' ')
      if k == ord(c):
        n.append([y, x, c])
    if n:
      hit += len(n)
      for z in n:
        m.remove(z)
    elif k != -1: # wrong key
      miss += 1
    now = time.time()
    if now - last < t:
      continue
    last += t
    n = []
    for y, x, c in m:
      if y < row - 1:
        n.append([y + 1, x, c])
      else:
        miss += 1
    m = n
    c = random.choice('abcdefghijklmnopqrstuvwxyz')
    if c == 'z':
      t *= 0.95
    m.append([0, random.randint(1, col - 2), c])
  return 'Final score is %d' % hit

print curses.wrapper(main)

