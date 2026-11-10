from animal import get_random_animal
from ai import call_gpt

def main():
    # Choose a random animal
    animal = get_random_animal()
    #let the user decide the mode
    mode = input("Easy mode? Type yes or no: ")
    if mode =="yes":
        rules = "Answer yes or no and add a short clue with it, like no but it has stripes. If the answer is same as animal say correct. Donot say anything else"
    else:
        rules = "Answe with only yes or no or correct, donot say anything else"
    # Print the initial message to the user
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    # Get their first guess
    question = input("Ask me a yes or no question: ")

    # Use GPT to get a yes, no, or correct
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else.{rules}"
    gpt_response = call_gpt(prompt)
    
    # Keep letting the user guess as long as its not correct
    while gpt_response != "Correct":
        # Output GPT's response
        print(f"{gpt_response}.")

        # Get the next question
        question = input("Ask me a yes or no question: ")

        # Use GPT to get the response
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else.{rules}"
        gpt_response = call_gpt(prompt)
    
    print("Correct!")

if __name__ == "__main__":
    main()
