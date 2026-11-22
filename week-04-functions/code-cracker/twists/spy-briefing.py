from ai import call_gpt
from random import randint
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

def spy_message(topic):
    prompt = f'''write a short secret spy message about {topic} and returns it in short case letters only'''
    message = call_gpt(prompt)
    return message

def main():
    print("Welcome to the Code Machine!")
    topic = input("Enter a topic: ")
    message = spy_message(topic)
    shift = randint(1,25)
    secret = encode(message, shift)
    print("Secret Briefing ", secret)
    input("Can you guess it, press enter to crack!")
    crack(secret)


if __name__ == "__main__":
    main()
