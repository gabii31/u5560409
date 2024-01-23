import random
n = random.randint(1,20) #n is the number
print('i am thinking of a number between 1 and 20')

print('take a guess')
i = int(input())

if i>n:
      print('too high')
elif i<n:
     print('too low')

       

if i == n:
   print('goodjob!')