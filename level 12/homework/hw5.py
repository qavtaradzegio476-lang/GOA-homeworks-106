#  შექმენით 8 ელემენტიანი რიცხვების სია. for ციკლის გამოყენებით იპოვეთ სიაში ყველაზე დიდი რიცხვი და დაბეჭდეთ იგი.
#  max() ფუნქციის გამოყენება არ შეიძლება.

numbers=[10, 20, 30, 40, 50, 60, 70, 80]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest) 

