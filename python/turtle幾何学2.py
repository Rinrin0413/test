from turtle import *
import random
speed(0)
width(width=2)
for i in range(500):
    codes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    color(f"#{codes[random.randint(0, 15)]}{codes[random.randint(0, 15)]}{codes[random.randint(0, 15)]}{codes[random.randint(0, 15)]}{codes[random.randint(0, 15)]}{codes[random.randint(0, 15)]}")
    right(random.randint(1, 360))
    left(random.randint(1, 360))
    fd(10)
done()
