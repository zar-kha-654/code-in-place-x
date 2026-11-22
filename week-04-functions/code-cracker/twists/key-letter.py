ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, n):
    position = ALPHABET.find(letter)
    new_position = (position + n) % len(ALPHABET)
    return ALPHABET[new_position]


def encode(message, n):
    result = ""
    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(letter, n)
        else:
            result += letter
    return result


def decode(message, n):
    return encode(message, -n)


def crack(message):
    for i in range(25):
        shift = i + 1
        decoded_message = decode(message, shift)
        print(f"Shift {shift}: {decoded_message}")

def letter_to_shift(key):
    shift = ALPHABET.find(key)
    return shift

def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    key = input("Enter a key letter: ")
    shift = letter_to_shift(key)
    secret = encode(message, shift)
    print("Secret", secret)


if __name__ == "__main__":
    main()
