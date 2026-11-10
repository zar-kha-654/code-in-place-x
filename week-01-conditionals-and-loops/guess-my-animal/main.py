from animal import get_random_animal
from ai import call_gpt
def main():
    animal = get_random_animal()
    # TODO: your code here!
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")
    while True: 
        answer = input("Ask me a yes or no question:")
        if answer == animal:
            print("Correct! ")
            break
        prompt = f'''User is playing guess my animal name, the name of animal is {animal}
        , user guess is {answer}, answer the user's yes or no answers in 'Yes' or 'No' only 
        donot reveal the animal's name.'''
        response = call_gpt(prompt)
        print(response)
            
if __name__ == "__main__":
    main()
