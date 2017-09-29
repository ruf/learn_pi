#!/usr/bin/python

import time, random, curses

def main(screen):
  curses.curs_set(0)
  screen.nodelay(True)
  row, col = screen.getmaxyx()
  m = [] # [[y, x, c] ... ]
  t = 1
  hit = miss = 0
  last = time.time()
  while miss < 20:
    n = []
    for y, x, c in m:
      try:
        screen.addstr(y, x, c, curses.A_BOLD)
      except:
        n.append([y, x, c])
        miss += 1
        t /= 0.95
    screen.box()
    screen.addstr(0, 2, '  Hit:%d  Miss:%d  Speed:%.2fX  ' % (hit, miss, 1 / t), curses.A_REVERSE)
    screen.refresh()
    time.sleep(0.05)
    k = screen.getch()
    if k == curses.KEY_UP:
      break
    old_hit = hit
    for y, x, c in m:
      screen.addstr(y, x, ' ')
      if k == ord(c):
        n.append([y, x, c])
        hit += 1
        if hit % 20 == 0:
          t *= 0.95
    for z in n:
      m.remove(z)
    if k != -1 and old_hit == hit: # wrong key
      miss += 1
    now = time.time()
    if now - last > t:
      last += t
      for z in m:
        z[0] += 1
      c = random.choice('abcdefghijklmnopqrstuvwxyz')
      m.append([1, random.randint(1, col - 2), c])
  return 'Final score is %d' % hit

print curses.wrapper(main)

