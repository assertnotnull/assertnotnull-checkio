def checkio(text):
    frequency = {}
    for char in [char for char in text.lower() if char.isalpha()]:
        frequency[char] = frequency.setdefault(char, 0) + 1
    letter = min([k for k, v in frequency.items() if v == max(frequency.values())])
    return letter


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."