# Displaying fibonacci series upto n terms

n = int(input("Enter the number of terms? "))

# Initialisation of 2 terms
n1, n2 = 0, 1
count = 0

# Checking for validation and printing the fibonacci series
if n <= 0:
   print("Please enter a positive integer!")
elif n == 1:
   print("Fibonacci series upto ", n, " terms :")
   print(n1)
else:
   print("Fibonacci series upto ", n, " terms :")
   while count < n:
       print(n1)
       nth = n1 + n2
       # updating values
       n1 = n2
       n2 = nth
       count += 1







