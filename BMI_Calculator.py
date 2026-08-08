def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in metres."""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    """Run the BMI calculator application."""

    print("=== BMI Calculator ===")

    try:
        # Get weight and height from the user
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        # Validate the input
        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Determine BMI category
        category = get_bmi_category(bmi)

        # Display the result
        print("\n--- BMI Result ---")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()