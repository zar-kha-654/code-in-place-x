from random import randint
from ai import call_gpt

def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        # Generate two random numbers
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        # Prompt the user with the problem
        prompt= f''' the user is trying a sum question
        you have to make it simpler by explaining the sum in one 
        line story like : Maya has 23 stickers and her friend gives her 45 more. How many stickers does Maya have now?
        , users numbers are {num1} and {num2}, donot say anything 
        else'''

        ai = call_gpt(prompt)
        print(ai)
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2

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
