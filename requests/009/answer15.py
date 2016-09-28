#!/usr/bin/python

for i in range(10000):
  j = i
  for n in range(5):
    if j % 5 != 1:
      break
    j = (j - 1) / 5 * 4
  else:
    if j % 5 == 0:
      print i
