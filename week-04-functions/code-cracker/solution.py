ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(message):
    for n in range(1,26):
        encoded = ""
        for letter in message:
            if letter in ALPHABET:
                word = ALPHABET.find(letter)
                shift1= (word - n)%26
                words = ALPHABET[shift1]
                encoded += words
            else:
                encoded += letter
                
        print(f"Shift {n}: {encoded}")
def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    shift_letter(message)
    
if __name__ == "__main__":
    main()
