import secrets


def ask_characters():
    while True:
        chars = input("Type the characters you wish to use in your password: ")
        if chars:
            return chars
        print("Please enter at least one character.")


def ask_length():
    while True:
        try:
            length = int(input("Type the length of your password: "))
            if length > 0:
                return length
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def ask_yes_no(prompt):
    return input(prompt).strip().lower() in ("y", "yes")


def generate_password(chars, length):
    return "".join(secrets.choice(chars) for _ in range(length))


def main():
    chars = ask_characters()
    length = ask_length()

    while True:
        print("\nYour random password is:")
        print(generate_password(chars, length))
        print()

        if not ask_yes_no("Would you like to generate another password (y/n)?: "):
            break

        if not ask_yes_no("Do you want to use the same set of characters (y/n)?: "):
            chars = ask_characters()

        if ask_yes_no("Would you like to redefine the length of your password (y/n)?: "):
            length = ask_length()


if __name__ == "__main__":
    main()