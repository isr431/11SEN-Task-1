class MoneyBuckets:
    def __init__(self):
        pass

    def get_income(self):
        while True:
            income = input("Enter income amount: ").strip("$")

            try:
                income = float(income)
            except:
                print("Please enter a valid number.")
            else:
                if income <= 0:
                    print("Income must be a positive number.")
                else:
                    self.income = income
                    break

    def calculate_buckets(self):
        blow = 0.6 * self.income
        daily_expense = 0.6 * blow
        splurge = 0.1 * blow
        smile = 0.1 * blow
        fire_extinguisher = 0.2 * blow

        grow = 0.2 * self.income
        mojo = 0.2 * self.income

        self.buckets = {
            "BLOW (60%)": {
                "total": blow,
                "description": "This should cover your daily expenses.",
                "Daily Expenses (60%)": {
                    "amount": daily_expense,
                    "description": "For your regular daily expenses like groceries, bills, etc."
                },
                "Splurge (10%)": {
                    "amount": splurge,
                    "description": "Short term treats e.g. movie tickets, takeaway coffees"
                },
                "Smile (10%)": {
                    "amount": smile,
                    "description": "Long term goals you need to save for e.g. STEM tour"
                },
                "Fire Extinguisher (20%)": {
                    "amount": fire_extinguisher,
                    "description": "For unexpected expenses (e.g. unexpected vet bill)"
                }
            },
            "GROW (20%)": {
                "amount": grow,
                "description": "To build long-term wealth and security"
            },
            "MOJO (20%)": {
                "amount": mojo,
                "description": "Safety money for emergencies"
            }
        }
    
    def display(self):
        print("\n" + "=" * 60)
        print(f"YOUR MONEY BUCKETS - Monthly Income: ${self.income:.2f}")
        print("=" * 60)

        for category, value in self.buckets.items():
            if "total" in value:
                print(f"\n{category}: ${value['total']:.2f}")
                print(f"    Description: {value['description']}")
                print("    Breakdown:")

                for subcategory, subvalue in value.items():
                    if subcategory not in ["total", "description"]:
                        print(f"    - {subcategory}: ${subvalue['amount']:.2f}")
                        print(f"      {subvalue['description']}")
            else:
                print(f"\n{category}: ${value['amount']:.2f}")
                print(f"    Description: {value['description']}")

    def run(self):
        self.get_income()
        self.calculate_buckets()
        self.display()

class CompoundInterest:
    def __init__(self):
        self.total_savings = 0

    def get_age(self):
        while True:
            age = input("Enter your age: ")

            try:
                age = int(age)
            except:
                print("Please enter a valid number.")
            else:
                if age < 0:
                    print("Age must be a positive number.")
                else:
                    self.age = age
                    break
    
    def get_interest(self):
        while True:
            interest = input("Enter the interest rate: ").strip("%")

            try:
                interest = float(interest)
            except:
                print("Please enter a valid number.")
            else:
                if interest < 0:
                    print("Interest rate must be a positive number.")
                else:
                    self.interest = interest / 100
                    break
    
    def get_amount(self):
        while True:
            amount = input("Enter the amount you want to invest per annum: ").strip("$")

            try:
                amount = float(amount)
            except:
                print("Please enter a valid number.")
            else:
                if amount < 0:
                    print("Amount must be a positive number.")
                else:
                    self.amount = amount
                    break
    
    def calculate_savings(self):
        while self.age <= 60:
            interest_earned = self.total_savings * self.interest
            self.total_savings += self.amount + interest_earned
            self.age += 1
    
    def run(self):
        self.get_age()
        self.get_interest()
        self.get_amount()
        self.calculate_savings()

        print(f"Total savings: {self.total_savings}")

while True:
    mode = input("Select mode (money buckets/compound interest): ").lower()

    if mode == "money buckets":
        money_buckets = MoneyBuckets()
        money_buckets.run()
        break
    elif mode == "compound interest":
        compound_interest()
        break
    else:
        print("Invalid mode.")