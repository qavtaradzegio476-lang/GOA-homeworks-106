#  შექმენით სია რომელშიც გექნებათ მინიმუმ 10 რიცხვი, შემდეგ:

# - დაითვალეთ, რამდენი დადებითი რიცხვია;
# - რამდენი უარყოფითი;
# - რამდენი ნულის ტოლი.
# - ბოლოს დაბეჭდეთ სამივე შედეგი

numbers = [ 10, 20, 30, 40, 0, -1, 1000, 93, 43, 23]

positive =0
negative = 0
zero = 0

for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1

print(positive)
print(negative)
print(zero)        
   

