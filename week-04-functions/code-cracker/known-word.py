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


def crack(message,clue):
    for i in range(25):
        shift = i + 1
        decoded_message = decode(message, shift)
        if clue in decoded_message:
            print(f"Shift {shift}: {decoded_message}")


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    clue = input("A word you think is in it: ")
    crack(message,clue)


if __name__ == "__main__":
    main()
