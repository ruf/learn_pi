#!/usr/bin/python
# *-* coding:utf-8 *-*

m = {}
is_body = False

for s in file('唐诗三百首.txt').readlines():
  if not is_body:
    if '作者：' in s:
      is_body = True
  elif '【注解】' in s:
    is_body = False
  else:
    for x in s.strip().decode('utf-8'):
      if x in m:
        m[x] += 1
      elif not x in u'，。！？《》“”':
        m[x] = 1
k = sorted(m, key=m.get, reverse=True)
for j in k[:30]:
  print j.encode('utf-8'), m[j], '\t\t',
print
