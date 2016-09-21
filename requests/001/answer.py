#!/usr/bin/python

m = {k for k in range(101,113)}
f = {k for k in range(101,113)}

while True:
 cio = input('What can I help you (1-check in, 2-check out) ? ')
 if cio == 1:
  if len(f) > 0:
   rn = list(f)[0]
   f.remove(rn)
   print 'Your room number is %i, this is your room key.' % rn
  else:
   print "Sorry we don't have free room now."
 if cio == 2:
  rn = input('What is your room number ? ') 
  if rn in m:
   if not rn in f:
    f.add(rn)
    print 'Thank you, good bye.'
   else:
    print 'This room is not allocated yet.'
  else:
   print 'Sorry the room number is wrong.'
 if len(f) > 0:
  print 'There are %i free rooms.' % len(f)
 else:
  print 'No free rooms.'
