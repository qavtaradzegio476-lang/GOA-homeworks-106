# მომხმარებლისგან მიიღეთ ქულა (0-100) და if / elif / else-ის გამოყენებით განსაზღვრეთ შეფასება:
# - 90-100 → A
# - 80-89 → B
# - 70-79 → C
# - 60-69 → D
# - დანარჩენი → F

score=int(input("please enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")    
elif score >= 60:
    print("D")
else:
    print("F")