#!/usr/bin/python

m = {101:'f',102:'f',103:'f',104:'f',105:'f',106:'f',107:'f',108:'f',109:'f',110:'f',111:'f',112:'f'}
m = {k:'f' for k in range(101,113)}
while True:
 cio = input('What can I help you (1-check in, 2-check out) ? ')
 if cio == 1:
  f = False
  for k in m:
   if m[k] == 'f':
    f = True
    print 'Your room number is %i, this is your room key.' % k
    m[k] = 'u'
    break
  if f == False:
   print "Sorry we don't have free room now."
 if cio == 2:
  rn = input('What is your rom number ? ') 
  if rn in m:
   if m[rn] == 'u':
    m[rn] = 'f'
    print 'Thank you, good bye.'
   else:
    print 'This room is not allocated yet.'
  else:
   print 'Sorry the room number is wrong.'
 n = 0
 for k in m:
  if m[k] == 'f':
   n += 1
 if n > 0:
  print 'There are %i free rooms.' % n
 else:
  print 'No free rooms'
 
