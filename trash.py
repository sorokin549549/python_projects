
def caesar(alphabet):
    text = input("Text: ")
    shift = ii("Shift: ")

    def get_char(char, alphabet_, shift_):
        if char.isalpha():
            i = 0
            if char.isupper():
                i = 1
            return alphabet_[i][(alphabet_[i].index(char) + shift_) % len(alphabet_[0])]
        return char

    shifted = "".join([get_char(char, alphabet, shift) for char in text])
    print(shifted)


def english_alphabet():A
    return "".join([chr(char) for char in range(ord("a"), ord("z") + 1)])


def ii(message=""):
    return int(input(message))


caesar([english_alphabet(), english_alphabet().upper()])