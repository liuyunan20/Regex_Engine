# please do not modify the following code
interest_rates = [float(x) for x in input().split(',')]
years = [int(x) for x in input().split(',')]
loan_principles = [int(x) for x in input().split(',')]

# your code here
zipped = zip(interest_rates, years, loan_principles)
for rate, year, principle in zipped:
    print(int(rate * year * principle))
