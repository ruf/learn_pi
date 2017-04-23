#!/usr/bin/python

from datetime import date

for y in range(2008, 2018):
  for m in (1, 3, 5, 7, 8, 10, 12):
    if date(y, m, 1).weekday() + 1 == 7:
      print y, m, ' ',
