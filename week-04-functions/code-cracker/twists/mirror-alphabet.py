ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(letter, n):
    position = ALPHABET.find(letter)
    new_position = (position + n) % len(ALPHABET)
    return ALPHABET[new_position]


def encode(message, n):
    result = ""
    for letter in message:
        if letter in ALPHABET:
            result += shift_letter(l, n)
        else:
            result += letter
    return result

def mirror(message,k):
    result = ""
    for letter in message:
        if letter in ALPHABET:
            result += mirror_letter(letter)
        else:
            result += letter
    return result

def decode(message, n):
    return encode(message, -n)

def mirror_letter(letter):
    position  = ALPHABET.find(letter)
    return ALPHABET[25-position]


def crack(message):
    for i in range(25):
        shift = i + 1
        decoded_message = decode(message, shift)
        print(f"Shift {shift}: {decoded_message}")


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    r=2
    secret = mirror(message, r)
    print("Mirrored: ", secret)
    print("Mirrored again: ", mirror(secret, r))


if __name__ == "__main__":
    main()
