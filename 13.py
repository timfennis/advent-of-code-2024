from z3 import *
import re

file = open("input/2024/13.txt").read().strip()

for part in [0, 10000000000000]:
    ans = 0
    for group in file.split("\n\n"):
        a, b, p = group.split("\n")
        ax, ay = map(int, re.findall(r"\d+", a))
        bx, by = map(int, re.findall(r"\d+", b))
        tx, ty = map(int, re.findall(r"\d+", p))

        tx += part
        ty += part

        ap = Int('ap')
        bp = Int('bp')
        y = Real('y')
        s = Solver()
        s.add(ap * ax + bp * bx == tx)
        s.add(ap * ay + bp * by == ty)
        if s.check() == sat:
            m = s.model()
            ans += m[ap].as_long() * 3 + m[bp].as_long()

    print(ans)