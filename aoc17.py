# -*- coding: utf-8 -*-

from blist import blist

lock_param = 335
lock = blist([0])
p = 0
c = 2017 # 50000000

for i in range(1, c + 1):
    p = (p + lock_param) % i + 1
    lock.insert(p, i)

print lock[lock.index(2017) + 1]

p = 0
c = 50000000
after_zero = -1
for i in range(1, c + 1):
    p = (p + lock_param) % i + 1
    if p == 1:
        after_zero = i
        print after_zero

print 'result', after_zero