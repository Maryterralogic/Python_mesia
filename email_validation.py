import re


def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def write_to_file(email):
    with open('email_list.txt', 'a') as file:
        file.write(email + '\n')


def read_from_file():
    with open('email_list.txt', 'r') as file:
        email_list = file.readlines()
        return [email.strip() for email in email_list]


def main():
    while True:
        user_input = input("Do you want to validate an email address? (Yes/No): ").strip().lower()

        if user_input == 'no':
            emails = read_from_file()
            if emails:
                print("List of email IDs:")
                for email in emails:
                    print(email)
            else:
                print("No email IDs in the list.")
            break

        if user_input == 'yes':
            email = input("Enter an email address: ").strip()
            if validate_email(email):
                write_to_file(email)
                print("Email address is valid and has been written to the file.")
            else:
                print("Email address is not valid.")


if __name__ == "__main__":
    main()
