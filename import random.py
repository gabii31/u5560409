import random
n = random.randint(1,20) #n is the number
print('i am thinking of a number between 1 and 20')

for times in range(1,7):
      print('take a guess')
      i = int(input())

      if i>n:
            print('too high')
      elif i<n:
            print('too low')
      else:
            break

      if i == n:
            print('goodjob!')
      else:
            print("the number i was thinking of was str(n))
