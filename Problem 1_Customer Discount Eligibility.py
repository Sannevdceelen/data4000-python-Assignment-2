# Problem 1: Customer Discount Eligibility
# A store offers discounts to its customers based on their membership status and total purchase amount.

def main():
    amount = float(input("Enter the total purchase amount: $"))
    membership = input("Enter the customer membership status (yes/no): ").strip().lower()
    
    if membership == "yes" and amount >= 100:
        discount_rate = 0.15
    elif membership == "yes" and amount < 100:
        discount_rate = 0.10
    elif membership == "no" and amount >= 150:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount = amount * discount_rate
    final_amount = amount - discount
   
    print(f"Discount applied: {discount_rate * 100:.2f}%")
    print(f"Final price after discount: ${discount:,.2f}")

if __name__ == "__main__":
    main()

