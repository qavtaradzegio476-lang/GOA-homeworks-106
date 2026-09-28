#  მომხმარებლისგან მიიღეთ სამი რიცხვი. if / elif / else-ის გამოყენებით განსაზღვრეთ:
# - თუ სამივე ტოლია → დაბეჭდეთ "ყველა რიცხვი ტოლია"
# - თუ რომელიმე ორი ტოლია → დაბეჭდეთ "ორი რიცხვი ტოლია"
# - წინააღმდეგ შემთხვევაში → დაბეჭდეთ "ყველა რიცხვი განსხვავებულია"

num1=int(input("please enter your first number: "))
num2=int(input("please enter your second number: "))
num3=int(input("please enter your third number: "))

if num1 == num2 and num2 == num3:
    print("ყველა რიცხვი ტოლია: ")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("ორი რიცხვი ტოლია: ")
else:
    print("ყველა რიცხვი განსხვავებულია")       
    