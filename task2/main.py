from collections import deque


def is_palindrome(input_string):
    formatted_string = "".join(input_string.lower().split())
    char_deque = deque(formatted_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


def main():
    """Головна функція для приймання вводу від користувача та виходу з програми."""
    while True:
        user_input = input(
            "Будь ласка, введіть рядок для перевірки або 'exit' для виходу: "
        )
        if user_input.lower() == "exit":
            print("Завершення програми.")
            break
        result = is_palindrome(user_input)
        if result:
            print("Введений рядок є паліндромом.")
        else:
            print("Введений рядок не є паліндромом.")


if __name__ == "__main__":
    main()
