#!/usr/bin/python

import time, random, curses

def main(screen):
  curses.curs_set(0)
  screen.nodelay(True)
  row, col = screen.getmaxyx()
  m = {} # (y, x)->c
  t = 1
  hit = miss = last = 0
  while miss < 100:
    for y, x in m:
      screen.addstr(y, x, m[y, x], curses.A_BOLD)
    screen.addstr(0, 0, '  Hit:%d  Miss:%d T:%.2f  ' % (hit, miss, t), curses.A_REVERSE)
    screen.refresh()
    time.sleep(0.05)
    c = screen.getch()
    if c == curses.KEY_UP:
      break
    d = hit
    for y, x in m:
      screen.addstr(y, x, ' ')
      if c == ord(m[y, x]):
        hit += 1
        m[y, x] = ' '
    if d == hit and c != -1:
      miss += 1
    now = time.time()
    if now - last < t:
      continue
    last = now
    n = {}
    for y, x in m:
      if m[y, x] == ' ':
        continue
      if y > row - 2:
        miss += 1
      else:
        n[y + 1, x] = m[y, x]
    m = n  
    c = random.choice('abcdefghijklmnopqrstuvwxyz')
    if c == 'z':
      t *= 0.95
    m[0, random.randint(1, col - 2)] = c
  return 'Hit:%d  Miss:%d ' % (hit, miss)

print curses.wrapper(main)

