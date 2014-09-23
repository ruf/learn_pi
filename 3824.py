#!/usr/bin/python

import os


q = [ float(x) for x in os.sys.argv[1:] ]
if len(q) != 4:
    print 'usage :', os.sys.argv[0], 'A B C D'
    os.sys.exit(0)

e = set()
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if a != b and a != c and a != d and b != c and b != d and c != d: 
                    e.add((q[a], q[b], q[c], q[d]))
f = set()
for a in ('+', '-', '*', '/'):
    for b in ('+', '-', '*', '/'):
        for c in ('+', '-', '*', '/'):
            f.add((a, b, c))

q = '''
%f%s%f%s%f%s%f
(%f%s%f)%s%f%s%f
%f%s(%f%s%f)%s%f
%f%s%f%s(%f%s%f)
(%f%s%f%s%f)%s%f
%f%s(%f%s%f%s%f)
(%f%s%f)%s(%f%s%f)
%f%s((%f%s%f)%s%f)
%f%s(%f%s(%f%s%f))
'''

z = ''
n = 0
for p in q.split():
    for x in e:
        for y in f:
            a = p % (x[0], y[0], x[1], y[1], x[2], y[2], x[3])
            try:
                b = eval(a)
                if b > 23.99 and b < 24.01:
                    a = p.replace('f', 'u') % (x[0], y[0], x[1], y[1], x[2], y[2], x[3])
                    n += 1
                    print n, ':', a
                    if z == '' or len(z) > len(a):
                        z = a
            except Exception, error:
                pass

            
print 'best result :', z
