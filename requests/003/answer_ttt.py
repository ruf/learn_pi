#!/usr/bin/python

b = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(-1, 9):
  if i < 0:
    print ' 7 | 8 | 9 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 1 | 2 | 3 \n'
  else:
    if i % 2 == 0:
      while True: 
        O = input('O, Where to place?')
        if O in range(1, 10):
          if not b[O] in ('O', 'X'):
            b[O] = 'O'
            print ' %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n'% (b[7], b[8],  b[9], b[4], b[5], b[6], b[1], b[2], b[3])
            break
          else:
            print 'Bad input! This number is in O or X.'
        else:
          print 'Bad input! This is not in the table.'
      if b[1] == b[2] and b[1] == b[3] or b[4] == b[5] and b[4] == b[6] or b[7] == b[8] and b[7] == b[9] or b[1] == b[4] and b[1] == b[7] or b[2] == b[5] and b[2] == b[8] or b[3] == b[6] and b[9] == b[3] or b[3] == b[5] and b[7] == b[3] or b[1] == b[5] and b[1] == b[9]:
        print 'O win.'
        break
    else:
      while True:
        X = input('X, Where to place?')
        if X in range(1, 10):
          if not b[X] in ('O', 'X'):
            b[X] = 'X'
            print ' %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n'% (b[7], b[8], b[9], b[4], b[5], b[6], b[1], b[2], b[3])
            break
          else:
            print 'Bad input! This number is in O or X.'
        else:
          print 'Bad input! This is not in the table.'
      if b[1] == b[2] and b[1] == b[3] or b[4] == b[5] and b[4] == b[6] or b[7] == b[8] and b[7] == b[9] or b[1] == b[4] and b[1] == b[7] or b[2] == b[5] and b[2] == b[8] or b[3] == b[6] and b[9] == b[3] or b[3] == b[5] and b[7] == b[3] or b[1] == b[5] and b[1] == b[9]:
        print 'X win.'
        break
print 'Draw.'
