def main():
    # Get user's weight and height
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    # Calculate BMI
    bmi = weight / (height * height)

    # Display BMI
    print(f"\nYour BMI is: {bmi:.2f}")

    # Display BMI category
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obesity")


if __name__ == "__main__":
    main()