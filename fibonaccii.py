n = int (input("Enter the nth term of fibonacci:"))
def calculate (n) :
    if n <= 0 :
        return "Error"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence [i-2])
    return sequence[-1]
num = calculate(n)
print(num) 