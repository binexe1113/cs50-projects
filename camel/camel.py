import re

def main():
    def camel_to_snake(arg1):
        snake = re.sub(r"([A-Z])", r"_\1", arg1)
        snake = snake.lower()
        return snake

    camel = input("CamelCase: ")
    snake = camel_to_snake(camel)
    print ("snake_case:", snake)

main()
