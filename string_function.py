def count_duplicates(lst):
    return len(lst) - len(set(lst))

def main():
    try:
        # Read a string from the command line
        user_input = input("Enter a string: ")

        if not user_input:
            raise ValueError("Input cannot be empty.")

        # Total number of characters in the statement
        total_characters = len(user_input)

        # Total number of duplicate characters
        duplicate_characters = count_duplicates(user_input)

        # Total number of words in the statement
        words = user_input.split()
        total_words = len(words)

        # Total number of duplicate words
        duplicate_words = count_duplicates(words)

        # Reverse the characters and words
        reversed_chars = user_input[::-1]
        reversed_words = ' '.join(reversed(words))

        # Form a new statement from the reversed words
        new_statement = reversed_words

        # Remove duplicate characters from the latest statement
        unique_chars = ''.join(sorted(set(new_statement), key=new_statement.index))

        # Print the results
        print("Total number of characters:", total_characters)
        print("Total number of duplicate characters:", duplicate_characters)
        print("Total number of words:", total_words)
        print("Total number of duplicate words:", duplicate_words)
        print("Reversed characters:", reversed_chars)
        print("Reversed words:", reversed_words)
        print("New statement from reversed words:", new_statement)
        print("Statement with duplicate characters removed:", unique_chars)

    except ValueError as ve:
        print("ValueError:", ve)
    #except IndexError as ie:
     #   print("IndexError:", ie)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
