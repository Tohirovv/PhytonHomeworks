def invest(amount, rate,  years ):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

principal = float(input("Enter initial amount: "))
annual_rate = float(input("Enter annual rate (as a decimal): "))
years = int(input("Enter number of years: "))

invest(principal, annual_rate, years)