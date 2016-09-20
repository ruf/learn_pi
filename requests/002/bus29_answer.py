#!/usr/bin/python

max = 40
now = 0
free = 40
x = 0

for sn in range(1, 9):
  print '[BUS 29 STOP %i]'%sn
  while sn == 1:
    on = input('How many people get on?')
    if on > max:
      print 'Bad input!There are only %i free seats on the bus.'%max
    else:
      now = x = on
      free -= on
      break
  if sn != 1 and sn != 8:
    while True:
      off = input('How many people get off?')
      if now - off < 0:
        print 'Bad input!There are only %i people on the bus.'%now
      else:
        now -= off
        free += off
        break
    while True:
      on = input('How many people get on?')
      if now + on > max:
        print 'Bad input!There are only %i free seats on the bus.'%free
      else:
        now += on
        free -= on
        if now > x:
          x = now
        break
    else:
      print '%i people get off.'%now
print 'There are up to %i people on the bus.'%x
