score1 = float(input("กรุณาใส่คะแนนเก็บของคุณเต็ม 30 ได้: "))
score2 = float(input("กรุณาใส่คะแนนสอบกลางภาคของคุณเต็ม 30 ได้: "))
score3 = float(input("กรุณาใส่คะแนนสอบปลายภาคของคุณเต็ม 40 ได้: "))
score=(score1+score2+score3)
if score >= 80:
    grade = "A"
elif score >= 75:
    grade = "B+"
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = "C+"
elif score >= 60:
    grade = "C"
elif score >= 55:
    grade = "D+"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print("คะแนนรวมของคุณคือ:", score)
print("เกรดของคุณคือ:", grade)