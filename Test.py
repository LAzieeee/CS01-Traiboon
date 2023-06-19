In_class_score = int(input())
midterm_score = int(input())
final_score = int(input())
all = In_class_score + midterm_score + final_score
if 80 <= all <= 100:
  print("A")
elif 75 <= all <= 79:
  print("B+")
elif 70 <= all <= 74:
  print("B")
elif 65 <= all <= 69:
  print("C+")
elif 60 <= all <= 64:
  print("C")
elif 55 <= all <= 59:
  print("D+")
elif 50 <= all <= 54:
  print("D")
elif all <= 40:
  print("F")
