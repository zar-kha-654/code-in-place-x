LETTERS = ["a", "c", "e", "i", "o", "t"]
EMOJIS = ["🍎", "🐱", "🥚", "🍦", "🐙", "🌮"]
# Asks the user for words and their emoji until they press enter, and returns the dictionary.
def build_emoji_dict():
    emoji_dict = {}
    word = input("Word: ")
    word = word.lower()
    while word != "":
        emoji = input(f"Emoji for {word}: ")
        emoji_dict[word] = emoji
        word = input("Word: ")
        word = word.lower()
    return emoji_dict


# Prints every word in the dictionary next to its emoji.
def print_emoji_dict(emoji_dict):
    for word in emoji_dict:
        emoji = emoji_dict[word]
        print(f"{word}: {emoji}")


# Swaps every word that has an emoji for its emoji. Other words stay the same.
def translate(sentence, emoji_dict):
    result = ""
    words = sentence.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in emoji_dict:
            emoji = emoji_dict[lower_word]
            result += emoji + " "
        else:
            result += word + " "
    return result

def build_alphabet(LETTERS, EMOJIS):
    alhphabet = {}
    for i in range (len(LETTERS)):
        letter = LETTERS[i]
        emoji = EMOJIS[i]
        alhphabet[letter] = emoji
    return alhphabet

def main():
    alhphabet = build_alphabet(LETTERS, EMOJIS)
    print_emoji_dict(alhphabet)


if __name__ == "__main__":
    main()
