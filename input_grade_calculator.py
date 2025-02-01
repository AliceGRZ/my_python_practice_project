# Write a program that asks for a student's score (out of 100) and assigns a grade based on the score:

# 90 and above: "A"
# 80 to 89: "B"
# 70 to 79: "C"
# 60 to 69: "D"
# Below 60: "F"

score = int(input("Please enter your score: "))

if score >= 90 and score <= 100:
  print("Your score is " + f"{score}," + " Passed - Grade A")
  if score >= 95:
    print("Free pass to University")

elif score >= 80 and score <= 89:
  print("Your score is " + f"{score}," + " Passed - Grade B")

elif score >= 70 and score <= 79:
  print("Your score is " + f"{score}," + " Passed - Grade C")

elif score >= 60 and score <= 69:
  print("Your score is " + f"{score}," + " Failed - Grade D")

elif score >= 0 and score <= 59:
  print("Your score is " + f"{score}," + " Failed - Gade F")

else:
  print ("Error occured")
