# NOTE; This was fancy to begin with anyways; I just liked it :)

# Display instructions for the whole program.
def display_instructions():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")

# Verify the input is either "D", "d", "a", or "A"
def validate_input(value):
    is_valid = False
    temp_value = value
    while is_valid == False:
        temp_value = input("Enter D, d, a, or A: ")
        if temp_value in("D", "d", "a", "A"):
            return temp_value
        else:
            print('Please answer with "D", "d", "a", or "A" only.')

# Takes in if answere if positive or negative and the person's answer.
# Calculates a score based on that and returns it. 
# Scores are, if positive, in order of D, d, a, A,;
# 0, 1, 2, 3 
def calculate_question_value(is_posititve, answer):
    score = -1
    if is_posititve:
        if answer == "D":
            score = 0
        elif answer == "d":
            score = 1
        elif answer == "a":
            score = 2
        else:
            score = 3
    else:
        if answer == "D":
            score = 3
        elif answer == "d":
            score = 2
        elif answer == "a":
            score = 1
        else:
            score = 0
    return score

def calculate_score(scores):
    total_score = sum(scores)
    return total_score


def main():
    # Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:
    display_instructions()
    scores = []
    questions = ["1. I feel that I am a person of worth, at least on an equal plane with others.",
     "2. I feel that I have a number of good qualities.", 
     "3. All in all, I am inclined to feel that I am a failure.", 
     "4. I am able to do things as well as most other people.", 
     "5. I feel I do not have much to be proud of.", 
     "6. I take a positive attitude toward myself.", 
     "7. On the whole, I am satisfied with myself.", 
     "8. I wish I could have more respect for myself.", 
     "9. I certainly feel useless at times.", 
     "10. At times I think I am no good at all."]
    is_positives = [True, True, False, True, False, True, True, False, False, False]
    for i in range(0, 10):
        print(questions[i])
        answer = "Z"
        answer = validate_input(answer)
        positive_bool = is_positives[i]
        score = calculate_question_value(positive_bool, answer)
        scores.append(score)
        print()
    final_score = calculate_score(scores)
    print(f"Your score is {final_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

# Execute program.
if __name__ == "__main__":
    main()