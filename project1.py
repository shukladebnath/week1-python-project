# BMI Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


# Main function
def main():

    print("BMI Calculator")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)

    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")


# Start the program
if __name__ == "__main__":
    main()