import random


def generate_number(difficulty):
    """Generates a number based on the difficulty set by the player"""
    generated_number = []
    numbers = 4
    minimum = 0
    easy_max = 5
    medium_max = 7
    hard_max = 9
    while True:
        if str(difficulty).isalpha() and str(difficulty).lower() == "easy":
            print("You've selected easy. The number will be between "
                  "0000 and 5555")
            for i in range(numbers):
                generated_number.append(str(random.randint(minimum, easy_max)))
        elif str(difficulty).isalpha() and str(difficulty).lower() == "medium":
            print("You've selected medium. The number will be between "
                  "0000 and 7777")
            for i in range(numbers):
                generated_number.append(
                    str(random.randint(minimum, medium_max)))
        elif str(difficulty).isalpha() and str(difficulty).lower() == "hard":
            print("You've selected hard. The number will be between "
                  "0000 and 9999")
            for i in range(numbers):
                generated_number.append(str(random.randint(minimum, hard_max)))
        return generated_number


def get_difficulty():
    """Get difficulty player desires"""
    while True:
        difficulty = input("Enter a difficulty (easy, medium, hard): ")
        if difficulty.lower() == "easy" or difficulty.lower() == "medium" \
                or difficulty.lower() == "hard":
            return difficulty
        else:
            print("Invalid entry. Please enter easy, medium or hard.")


def get_user_number():
    """Get number from user to be compared to the number generated from
    generate_number()"""
    guess_length = 4
    while True:
        value_entered = input("Enter a 4 digit integer or 'Q' to quit: ")
        if value_entered == "get key number":
            print(key_number)
        elif value_entered.upper() == "Q":
            exit(1)
        elif len(value_entered) < guess_length or len(value_entered) > \
                guess_length or value_entered.isnumeric() is False:
            print("Invalid entry. Please enter a 4 digit integer.")
        else:
            return value_entered


def number_of_matches(number_key, guess):
    """Determine the number of matches between the generated number and the
    player's guess"""
    matches = ""
    key_list = list(number_key)
    for i in guess:
        for j in key_list:
            if i == j:
                matches += "*"
                key_list.remove(j)
                break

    return matches


def numbers_are_equal(number_key, guess):
    """Return if the generated number and the guess are the same"""
    key_list = list(number_key)
    for i in range(len(key_list)):
        if key_list[i] != guess[i]:
            return False
    return True


def convert_to_number(number_key):
    """Output the generated number as an int"""
    number = ""
    for i in number_key:
        number += str(i)
    return int(number)


if __name__ == "__main__":
    while True:
        counter = 0
        matched = False

        key_number = generate_number(get_difficulty())
        while not matched:
            guessed_number = get_user_number()
            # print(key_number, guessed_number)
            counter += 1
            if numbers_are_equal(key_number, guessed_number):
                print("You guessed {} correctly. It took you {} tries".
                      format(convert_to_number(key_number), counter))
                matched = True
            else:
                print(number_of_matches(key_number, guessed_number))
