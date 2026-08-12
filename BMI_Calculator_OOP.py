class BMICalculator:

    def get_details(self):
        self.weight = float(input("Enter your weight in kg: "))
        self.height = float(input("Enter your height in metres: "))

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height * self.height)

    def display_result(self):
        print(f"\nYour BMI is: {self.bmi:.2f}")

        if self.bmi < 18.5:
            print("Category: Underweight")
        elif self.bmi < 25:
            print("Category: Normal weight")
        elif self.bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obesity")


# Create an object
calculator = BMICalculator()

# Call methods
calculator.get_details()
calculator.calculate_bmi()
calculator.display_result()