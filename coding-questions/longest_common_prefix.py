
def longest_common_prefix(user_input):
    for i, item in enumerate(user_input[0]):
        for string in user_input:
            if i>=len(string) or item!= string[i]:
                return user_input[0][:i]



if __name__ == "__main__":
    user_input =  ["flower", "flow", "flight"]

    output = longest_common_prefix(user_input)

    print(output)

