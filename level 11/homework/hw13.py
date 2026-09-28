#  მომხმარებლისგან მიიღეთ რიცხვი. while ციკლის გამოყენებით დაბეჭდეთ მხოლოდ ლუწი რიცხვები 1-დან მომხმარებლის მიერ შეყვანილი რიცხვის ჩათვლით.

number=int(input("please enter your number: "))

i=1

while i <= number:
    if i % 2 == 0:
        print(i)
    i += 1