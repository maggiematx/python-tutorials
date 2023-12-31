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
x=[1,2,3,4,5]
while x:
    print(x.pop(0))

# exercise 5: 
arr=np.arange(0,10)
arr

# exercise 6:
arr_reshaped=arr.reshape((2,5))
arr_reshaped

# exercise 7:
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

# exercise 8:
matrix1=np.arrange(1,10).reshape(3,3)
pring(matrix1)

# exercise 9:
matrix2=np.zeros([3,5])
matrix2

# exercise 10:
arr_num=[5,4,6,7,3]
bp_arr_num=np.array(arr_num)
