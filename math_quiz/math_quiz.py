import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within specified range.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random mathematical operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])

def calculate_result(num1, num2, operator):
    """
    Calculate the result of a mathematical expression.
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The mathematical operator.

    Returns:
        str: The formatted expression.
        int: The result of the expression.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    expression = f"{num1} {operator} {num2}"
    return expression, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz!")
    print("You will be presented with math problems, and you need to provide correct answer.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 9)
        num2 = generate_random_integer(1, 8)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
