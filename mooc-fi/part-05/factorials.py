# def calc_fact(n: int):
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i
#     return factorial



# def factorials(n: int):
#     factorials = {}

#     for i in range(1, n + 1):
#         factorials[i] = calc_fact(i)
#     return factorials

def factorials(n: int):
    factorials = {}

    factorials[1] = 1
    for i in range(2, n + 1):
        factorials[i] = factorials[i-1] * i

    return factorials