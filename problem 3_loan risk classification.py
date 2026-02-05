# problem 3 loan risk classification
# This program classifies loan risk based on credit score and annual income.

def main ():
    credit_score= int (input("Enter credit score: "))
    annual_income= float (input("Enter annual income: $"))

    if credit_score >= 720 and annual_income >= 60000:
        risk= "Low Risk"
    elif credit_score >= 650 and annual_income >= 40000:
        risk= "Medium Risk"
    else:
        risk= "High Risk"

    print("Loan Risk Classification:", risk)

if __name__ == "__main__":
    main()