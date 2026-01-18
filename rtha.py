import random as r
hero = r.randint(1, 30000)
hero1 = r.randint(1, 30000)
if hero1 > hero:
    print("no")
if hero > hero1:
    print("No")
if hero1 == hero:
    print("URAH!")