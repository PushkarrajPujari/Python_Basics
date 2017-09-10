# Demonstrating if elsif with exam marks example 
marks = 58
if marks < 0 or marks > 100:
    print("Invalid marks , Please enter valid marks")
elif 0 < marks < 35:
    print("Sorry , You Have failed")
elif 35 < marks < 50:
    print("You have cleared the exam with Passed Class")
elif 50 < marks < 60:
    print("You have cleared the exam with Second Class")
elif 60 < marks < 75:
    print("You have cleared the exam with First Class")
elif 75 < marks < 90:
    print("You have cleared the exam with distinction")
else:
    print("You have cleared the exam with merit")
