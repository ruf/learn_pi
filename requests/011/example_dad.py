#!/usr/bin/python
# coding: utf-8

from datetime import date

print '从2008年到2017年，有哪些月份包含5个星期日、星期一和星期二？'

for year in range(2008, 2018):
  for month in range(1, 13):
    m = { weekday:0 for weekday in range(7) }
    for day in range(1, 32):
      try:
        weekday = date(year, month, day).weekday()
        m[weekday] += 1
      except:
        pass
    if m[6] == 5 and m[0] == 5 and m[1] == 5:
      print '%d年%d月' % (year, month),


