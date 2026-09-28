# მომხმარებლისგან მიიღეთ ორი რიცხვი. თუ ერთ-ერთი მაინც ლუწია (or), დაბეჭდეთ "ერთ-ერთი მაინც ლუწია", წინააღმდეგ შემთხვევაში "ორივე კენტია".

num1=int(input("please enter your first number: "))
num2=int(input("please enter your second number: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print("ერთ-ერთი მაინც ლუწია")
else:
    print("ორივე კენტია")    