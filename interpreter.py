def main():
    expression = input("Expression: ")
    x, op, z = expression.strip().split()
    x = int(x)
    z = int(z)

    if op == "+":
        result = x + z
    elif op == "-":
        result = x - z
    elif op == "*":
        result = x * z
    elif op == "/":
        result = x / z

    print(f"{result:.1f}")

main()
