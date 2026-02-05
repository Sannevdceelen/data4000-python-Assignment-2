# Problem 1: Customer Discount Eligibility
# A store offers discounts to its customers based on their membership status and total purchase amount.

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_membership(prompt):
    while True:
        resp = input(prompt).strip().lower()
        if resp in ("yes", "no"):
            return resp
        print("Please enter 'yes' or 'no'.")


def main():
    total_purchase_amount = get_float("Enter the total purchase amount: $")
    customer_membership_status = get_membership("Enter the customer membership status (yes/no): ")

    if customer_membership_status == "yes" and total_purchase_amount >= 100:
        discount_rate = 0.15
    elif customer_membership_status == "yes" and total_purchase_amount < 100:
        discount_rate = 0.10
    elif customer_membership_status == "no" and total_purchase_amount >= 150:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    if discount_rate > 0:
        discount = total_purchase_amount * discount_rate
        final_amount = total_purchase_amount - discount
        print(f"Eligible for discount. Final discount {int(discount_rate*100)}%. Final amount after discount: ${final_amount:.2f}")
    else:
        print(f"Not eligible for discount. Final amount: ${total_purchase_amount:.2f}")


if __name__ == "__main__":
    main()

