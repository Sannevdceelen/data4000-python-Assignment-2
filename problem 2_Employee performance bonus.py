#problem 2_Employee performance bonus calculation

def main():
    salary = float(input("Enter annual salary: $ "))
    score = float(input("Enter performance score (0-100): "))

    if score >= 90:
        bonus_rate = 0.20 
    elif score >= 80:
        bonus_rate = 0.10
    elif score >= 70:
        bonus_rate = 0.05
    else:
        bonus_rate = 0.0

    bonus_amount = salary * bonus_rate

    print(f"Employee's bonus percentage: {bonus_rate * 100:.2f}%")
    print(f"Employee's performance bonus: ${bonus_amount:,.2f}")

if __name__ == "__main__":
    main()