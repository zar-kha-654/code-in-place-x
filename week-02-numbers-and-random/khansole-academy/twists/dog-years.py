
# Each calendar year is equal to 7.18 dog years
DOG_YRS_MULTIPLIER = 7.18

def main():
    age = int(input("Enter an age in calendar years: "))
    dog_years = DOG_YRS_MULTIPLIER * age
    print(f"That's {dog_years} in dog years!")

if __name__ == '__main__':
    main()
