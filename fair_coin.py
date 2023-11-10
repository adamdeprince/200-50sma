def factorial(x):
    m = 1
    for x in range(2,x+1):
        m *= x
    return m


def f(r, heads, tails):
    return factorial(heads + tails + 1) / (factorial(heads) * factorial(tails)) * r ** heads * (1-r) ** tails

