print("Easy Calc")

def do_calculation():
    math_type = input("Would you like to do 1) Addition, 2) Subtraction, 3) Multiplication, 4) Division: ")
    num_1 = float(input("Please enter your first number: "))
    num_2 = float(input("Please enter your second number: "))

    def addition_math():
        answer = num_1 + num_2
        print("Result: ", answer)

    def subtraction_math():
        answer = num_1 - num_2
        print("Result: ", answer)

    def multiplication_math():
        answer = num_1 * num_2
        print("Result: ", answer)

    def division_math():
        if num_2 == 0:
            print("THAT'S ILLEGAL!!!!!")
        else:
            answer = num_1 / num_2
            print("Result: ", answer)

    def do_math():
        if math_type == "1":
            addition_math()
        elif math_type == "2":
            subtraction_math()
        elif math_type == "3":
            multiplication_math()
        elif math_type == "4":
            division_math()
        else:
            print("You can't do that...")

    do_math()

    another_calculation = input("Would you like to do another calculation?: ")
    if another_calculation.lower() == "yes":
        do_calculation()
    else:
        print("Have a great day!")

do_calculation()
