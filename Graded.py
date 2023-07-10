score_1 = float(input("ใส่คะแนนเก็บของคุณ: "))
score_2 = float(input("ใส่คะแนนสอบกลางภาคของคุณ: "))
score_3 = float(input("ใส่คะแนนสอบปลายภาคของคุณ: "))
All_scores = score_1 + score_2 + score_3
if 0 <= score_1 <= 30 and 0 <= score_2 <= 30 and 0 <= score_2 <= 40:
    if 80 <= All_scores <= 100:
        print("A")
    elif 75 <= All_scores <= 79:
        print("B+")
    elif 70 <= All_scores <= 74:
        print("B")
    elif 65 <= All_scores <= 69:
        print("C+")
    elif 60 <= All_scores <= 64:
        print("C")
    elif 55 <= All_scores <= 59:
        print("D+")
    elif 50 <= All_scores <= 54:
        print("D")
    elif 0 <= All_scores <= 49:
        print("F")
elif 0 > score_1 or score_1 > 30 and 0 > score_2 or score_2 > 30 and 0 > score_3 or score_3 > 40: 
    print("โปรดใส่ข้อมูลให้ถูกต้องอีกครั้ง")


