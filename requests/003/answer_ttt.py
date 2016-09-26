#!/usr/bin/python

b = [ i for i in range(10) ]
for i in range(10):
  print '\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n'% (b[7], b[8],  b[9], b[4], b[5], b[6], b[1], b[2], b[3])
  if b[1] == b[2] == b[3] or b[4] == b[5] == b[6] or b[7] == b[8] == b[9] or b[1] == b[4] == b[7] or b[2] == b[5] == b[8] or b[3] == b[6] == b[9] or b[3] == b[5] == b[7] or b[1] == b[5] == b[9]:
    print p, 'win.'
    break
  if i == 9:
    print 'Draw.'
    break
  p = '\033[31m\033[1mO\033[0m'
  if i % 2 > 0:
    p = '\033[32m\033[1mX\033[0m'
  while True: 
    try:
      n = input(p + ', Where to place ? ')
      if n in range(1, 10) and b[n] in range(10):
        b[n] = p
        break
    except:
      pass
    print 'Bad input!'
