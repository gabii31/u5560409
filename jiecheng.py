def calculate_factorial(number):

    if number<0:
        return "Error"
    else:
        a = 1
        for i in range(1,number+1):
            a *= i
        return a 
     
    
    

print(calculate_factorial(5))
print(calculate_factorial(0))
print(calculate_factorial(3))
print(calculate_factorial(-1))
