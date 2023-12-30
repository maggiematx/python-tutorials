# exercise 1: simple multiplication 
x = 5
y = 4
print(x*y)

# exercise 2: find the maxmium number
x = 6
y = 7
z = 8
max_num = max(x,y,z)
print(f"The maximum number is: {max_num}")

# exercise 3: check for prime number
num = int(input(6))
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime")

#  exercise 4: 