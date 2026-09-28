#  შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა რიცხვი, მისი დავალებაა დააბრუნოს რიცხვების ჯამი 0 - იდან ამ გადმოცემულ რიცხვამდე.

def sum_numbers(number):
    total = 0

    for i in range(number + 1):
        total += i

    return total


print(sum_numbers(5))