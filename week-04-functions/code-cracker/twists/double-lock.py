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

def double_lock(message, n):
    once = encode(message, n)
    return encode(once, n)

def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    n= int(input("Enter a shift:"))
    secret = double_lock(message, n)
    print("Double locked: ", secret)



if __name__ == "__main__":
    main()
