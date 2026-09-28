# შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს დადებითი რიცხვების რაოდენობას ამ სიაში.

def count_positive(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count += 1

    return count


print(count_positive([5, -2, 8, 0, -4, 3]))