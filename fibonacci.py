def fibonacci_sequence(max_value):
    if max_value<0:
        return "Error"
    else:
        result= []
        a,b = 0,1
        while a <= max_value:
            result.append(a)
            a, b = b, a+b
        return result

print(fibonacci_sequence(10))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(-5))