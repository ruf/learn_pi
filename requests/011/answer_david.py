#!/usr/bin/python

from datetime import date

for y in range(2008, 2018):
  for m in range(1, 13):
    x = {}
    for d in range(1, 32):
      try:
        wday = (date(y, m, d).weekday()) + 1
        x[wday] = 1 if not wday in x else x[wday] + 1
      except:
        pass
    if (x[7], x[1], x[2]) == (5, 5, 5):
      print y,m,' ',
