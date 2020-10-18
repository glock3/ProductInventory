def read_input():
    name = input()
    description = input()
    some_number = input()
    return name, description, some_number


if __name__ == "__main__":

    result = read_input()
    print(result)
