def checkio(text):
    
    text = text.lower()
    
    max_freq = 0
    max_letter = ''
    
    for letter in text:
        if letter.isalpha():
            num = text.count(letter)
            if num > max_freq or num == max_freq and letter < max_letter:
                max_freq = num
                max_letter = letter
    print(max_letter)
    return max_letter

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
