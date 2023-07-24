x=float(input("ใส่ตัวเลขแทน x : "))
if x > 0:
    x = "x เป็นเลขบวก"
elif x == 0:
    x = "x เป็นเลขศูนย์"
else:
    x = "x เป็นเลขลบ"
print(x)