# o	Total bill < 500 → No discount
# o	500 to 1000 → 5% discount
# o	Above 1000 → 10% discount
# Take bill amount as input and display final amount to be paid.
bill=int(input("Enter A Total Bill Amount:-"))
if bill<=500:
    print("Sorry No Discount Availabel")
elif bill>500 and bill<=1000:
    print("5% Discount")
    disc=bill/5
    bill=bill-disc
    print(f"Bill After Discount:-{bill}")
elif bill>1000:
    print("10% Discount")
    di=bill/10
    bill=bill-di
    print(f"Total  Bill After Discount:-{bill}")
