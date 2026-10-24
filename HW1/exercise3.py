grade = int(input("Enter in grade from 0 to 100"))
if grade >= 90:
    print("A")
elif grade < 90 and grade >=75:
    print("B")
elif grade < 75 and grade >= 60:
    print("C")
else:
    print("F")