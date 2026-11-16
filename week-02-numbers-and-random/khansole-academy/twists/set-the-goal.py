from random import randint

def main():
    print("Khansole Academy")

    correct_in_a_row = 0
    goal = int(input("How many in a row do you want to get? "))

    while correct_in_a_row < goal:
        # Generate two random numbers
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        # Prompt the user with the problem
        print(f"What is {num1} + {num2}?")
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2
        print(true_ans)

        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
