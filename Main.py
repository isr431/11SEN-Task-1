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

def compound_interest():
    pass

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