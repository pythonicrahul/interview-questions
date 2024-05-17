# Reverse a string 

def slicing_solution(string):
    return string[::-1]

def loop_solution(string):
    output = ""
    for i in range(len(string) -1 , -1 , -1):
        output += string[i]
    return output

def two_pointer_approach(string):
    start = 0
    string = list(string)
    end = len(string) - 1

    while end > start:
        string[start], string[end] = string[end], string[start]
        start += 1
        end   -= 1
    
    return "".join(string)

if __name__ == "__main__":
    user_input = "question" or input("Enter input for finding the palindrone \n")
    output = slicing_solution(user_input)
    print("---" * 10)
    print(f"Input Given: {user_input}")
    print(f"Output: {output}")
    print("---" * 10)

    output = two_pointer_approach(user_input)
    print("---" * 10)
    print(f"Input Given: {user_input}")
    print(f"Output: {output}")
    print("---" * 10)


