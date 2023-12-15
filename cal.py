def calculate_zakat(wealth):
    # Nisab threshold for Zakat calculation (in currency, e.g., dollars, pounds, etc.)
    nisab = 345 # This value varies based on currency and current rates
    
    # Zakat rate (as a percentage)
    zakat_rate = 2.5
    
    if wealth < nisab:
        return 0  # If wealth is less than the Nisab threshold, no Zakat is due
    
    zakat_amount = wealth * (zakat_rate / 100)
    return zakat_amount

# Example usage:
wealth_amount = float(input("Enter your total wealth/assets amount: "))
zakat_due = calculate_zakat(wealth_amount)

print(f"The Zakat due on your wealth is: {zakat_due} units")
