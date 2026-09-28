#  შექმენით ფუნქცია, რომელიც მიიღებს ტექსტს და დააბრუნებს მასში ხმოვანი ასოების რაოდენობას. (aeiou)

def count_vowels(text):
    count = 0

    for letter in text:
        if letter in "aeiou":
            count += 1

    return count


print(count_vowels("hello"))