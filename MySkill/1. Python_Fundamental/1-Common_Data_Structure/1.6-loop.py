# while loop

num = 1
odd_number = []

while num:
      if num % 2 != 0:
        odd_number.append(num)
      if num >= 20:
          break
      num += 1
print('Odd numbers',odd_number)

# For Loop
list = [1,2,3,4,5]
list2 = []
for num in list:
    list2.append(num)

print(list2)