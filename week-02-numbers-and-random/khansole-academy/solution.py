
from random import randint

def main():
    print("Khansole Academy")

    count = 0

    while count < 3:
        num1 = randint(10, 99)
        num2 = randint(10, 99)
        total = num1 + num2

        print(f"What is {num1} + {num2}?")
        answer = int(input("Your answer: "))

        if answer == total:
            count += 1
            print("Correct!")
            print(f"You've gotten {count} correct in a row.")
        else:
            print("Incorrect.")
            print(f"The expected answer is {total}")
            count = 0

    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
