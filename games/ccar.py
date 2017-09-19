#!/usr/bin/python

import sys, time, random
from curses import wrapper

def main(screen):
  screen.nodelay(True)
  rows, columns = screen.getmaxyx()
  width = columns - 14
  road = width / 2
  left = (width - road) / 2
  car = road / 2
  d = 0
  for i in range(3000):
    e = {-1:'//', 0:'||', 1:'\\\\'}[d]
    print ('%4dm ' % i) + ' ' * left + e + ' ' * car + 'O=O' + ' ' * (road - car) + e, '\r',
    sys.stdout.flush() # show this line ASAP
    if car < 0 or car > road: # PONG!
      break
    try:
      c = screen.getkey()
      if c == 'x' or c == 'q':
        break
      if c == 'j' or c == '4' or c == 'KEY_LEFT':
        car -= 1
      if c == 'l' or c == '6' or c == 'KEY_RIGHT':
        car += 1
    except:
      pass # no input
    r = random.random()
    if r < 0.4 and d >= 0:
      d -= 1
    elif r > 0.6 and d <= 0:
      d += 1
    if left == 0 and d < 0 or left + road == width and d > 0:
      d = 0
    time.sleep(0.04)
    print ' ' * (6 + left) + e + ' ' * (3 + road) + e, '\r'
    left += d
    car -= d
    if r < 0.02:
      road -= 1
  return i

print 'Final score: %dm' % wrapper(main)

