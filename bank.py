def main():
    greeting = input("Greeting: ")
    normalized = greeting.strip().lower()

    if normalized.startswith("hello"):
        print("R0")
    elif normalized.startswith("h"):
        print("R20")
    else:
        print("R100")

main()
