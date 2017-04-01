#!/usr/bin/python
# -*- coding: utf-8 -*-

body, m = False, {}
for s in file('唐诗三百首.txt').readlines():
  if '【注解】：' in s:
    body = False
  elif '作者：' in s:
    body = True
  elif body:
    for c in s.strip().decode('utf-8'):
      if c in m:
        m[c] += 1
      elif not c in u'，。！？':
        m[c] = 1
for c in sorted(m, key=m.get)[-30:]:
  print c.encode('utf-8'), m[c]
