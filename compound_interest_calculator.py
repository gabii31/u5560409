def compound_interest_calculator(P, r, n, t):
    A = P*(1 + r/n)**(n*t)
    print (A)

compound_interest_calculator(1000, 0.05, 12, 5)
compound_interest_calculator(500, 0.07, 4, 10)
compound_interest_calculator(1500, 0.03, 6, 7)