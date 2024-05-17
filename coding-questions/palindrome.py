def palindrome_with_reverse(string):
    return string == string[::-1]

def two_pointer_approach(string):
    start = 0
    end = len(string) - 1

    while end > start:

        if string[end] != string[start]:
            return False
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    user_input = "question" or input("Enter input for finding the palindrone \n")
    output = palindrome_with_reverse(user_input)
    print("---" * 10)
    print(f"Input Given: {user_input}")
    print(f"Output: {output}")

    output = two_pointer_approach(user_input)

    print("---" * 10)
    print(f"Input Given: {user_input}")
    print(f"Output: {output}")