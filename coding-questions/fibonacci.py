# PENDING

def fibonacci(n):

    a = 0
    b = 1
    output = [0 , 1]
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    for _ in range(2, n):
        output.append(output[-1] + output[-2])

    return output


if __name__ == "__main__":
    output = fibonacci(10)
    print(output)