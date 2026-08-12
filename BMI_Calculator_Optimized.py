def isfloat(n):
    """Convert a value to float or return False if invalid."""
    try:
        return float(n)
    except ValueError:
        return False


def inputfloat(hint):
    """Keep asking until the user enters a valid number."""
    while True:
        value = isfloat(input(hint))

        if value is not False:
            return value

        print("Please enter a number.")


class BMIcalculator:

    def getdata(self):
        """Get weight in kg and height in cm."""
        self.w = inputfloat("Please enter your weight in kilograms: ")
        self.h = inputfloat("Please enter your height in centimetres: ") / 100

    def calculate(self):
        """Calculate BMI."""
        self.bmi = round(self.w / (self.h ** 2), 2)

    def display_result(self):
        """Display BMI and category."""
        print(f"\nYour BMI is: {self.bmi}")

        if self.bmi < 18.5:
            print("Category: Underweight")
        elif self.bmi < 25:
            print("Category: Normal weight")
        elif self.bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obesity")


def main():
    print("\n" + "=" * 42)
    print("Hello, let's calculate your BMI.\n")

    calc = BMIcalculator()

    calc.getdata()
    calc.calculate()
    calc.display_result()

    print("=" * 42)


if __name__ == "__main__":
    main()