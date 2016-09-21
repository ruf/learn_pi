#!/usr/bin/python

stops = 8
seats = 40
now = 0
x = 0

for sn in range(1, stops + 1):
  print '[BUS 29 STOP NO. %i]' % sn
  if sn == 1:
    while True:
      on = input('How many people get on? ')
      if on <= seats:
        now = x = on
        break
      print 'Bad input! There are only %i free seats on the bus.' % seats
  elif sn == stops:
      print '%i people get off.' % now
  else:
    while True:
      off = input('How many people get off? ')
      if now >= off:
        now -= off
        break
      print 'Bad input!There are only %i people on the bus.' % now
    while True:
      on = input('How many people get on? ')
      if now + on <= seats:
        now += on
        if now > x:
          x = now
        break
      print 'Bad input! There are only %i free seats on the bus.' % (seats - now)
print 'There were up to %i people on the bus.' % x
