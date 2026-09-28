# შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მეორე ყველაზე დიდ რიცხვს.
#  გაითვალისწინეთ შემთხვევა, როდესაც სიაში საკმარისი განსხვავებული რიცხვი არ არის.

def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


print(second_largest([5, 8, 2, 10, 7]))