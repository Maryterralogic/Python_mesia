class ATM:
    def __init__(self):
        self.denominations = [500, 200, 50]

    def validate_amount(self, amount):
        if amount <= 0 or amount % self.denominations[-1] != 0:
            return False
        return True

    def calculate_notes(self, amount):
        notes_count = {}
        for denomination in self.denominations:
            if amount >= denomination:
                count = amount // denomination
                notes_count[denomination] = count
                amount -= count * denomination
        return notes_count

    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid amount for withdrawal.")
            return

        notes_count = self.calculate_notes(amount)

        total_dispensed = 0
        print("Withdrawal successful. Here's your money:")
        for denomination, count in notes_count.items():
            print(f"{denomination} notes: {count}")
            total_dispensed += denomination * count
        print("Total amount dispensed:", total_dispensed)


# Main program
atm = ATM()

while True:
    withdrawal_amount = int(input("Enter the amount to withdraw: "))

    atm.withdraw(withdrawal_amount)

    choice = input("Do you want to continue (C) or cancel (X)? ").upper()
    if choice != "C":
        print("Transaction canceled.")
        break
