
def case_counter(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count +=1
        elif char.islower():
            lower_count +=1
        
    print("uppercase letters:", upper_count)
    print("lowercase letters:", lower_count)

case_counter("Hello,World!")
case_counter("PYTHON") 
case_counter("python")  
case_counter("1234!@#$")
