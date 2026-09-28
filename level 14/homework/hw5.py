#  მომხმარებელს შეაყვანინე წინადადება და შემდეგ საძიებელი სიტყვა. find() ფუნქციის გამოყენებით იპოვე, რომელ პოზიციაზე იწყება ეს სიტყვა წინადადებაში. თუ სიტყვა არ მოიძებნა,
#  დაბეჭდე შესაბამისი შეტყობინება.

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

position = sentence.find(word)

if position == -1:
    print("სიტყვა ვერ მოიძებნა")
else:
    print(position)