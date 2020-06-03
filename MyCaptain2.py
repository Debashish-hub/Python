#Positive Numbers in a list

# Take the input
# creating an empty list
list1 = []
# number of elemetns as input
list1 = [int(item) for item in input("Enter the list items : ").split()]
  
    
print("Positive Numbers are :")
# iterating each number in list 
for num in list1:     
    # checking condition 
    if num >= 0: 
       print(num, end = " ") 