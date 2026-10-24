age = int(input("Enter in age"))
gpa = int(input("enter in gpa"))

if age >= 18 and gpa >= 3:
    print("eligible")
elif age < 18 or gpa > 3.8:
    print("special consideration")
else:
    print("not eligible")