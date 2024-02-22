import turtle

def koch_snowflake(turtle, iterations, length):
    if iterations == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, iterations-1, length/3)
            turtle.left(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)

    iterations = int(input("Введіть рівень рекурсії: "))

    for _ in range(3):
        koch_snowflake(snowflake, iterations, 300)
        snowflake.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()