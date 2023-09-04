# without py dictionary

def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in universe'
    }

    while True:
        word = input("Enter the word you want to see meaning: ")
        if word != word_dictionary:
            print("Not in dictionary try again")
        if word in word_dictionary:
            print(f"{word} : {word_dictionary[word]}")


main()
