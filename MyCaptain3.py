# Assigning elements to different lists

# Initialising different lists
list1 = []
list2 = [1,45,67]

#Adding single element to lists
list1.append(5)
list2.append(3)

#Printing the lists
print("List after adding single element:")
print(list1)      #[5]
print(list2)      #[1, 45, 67, 3]

#Adding multiple elements to lists
list1.extend([12,43,56,78])       
list2.extend([30,41,0])           
#Printing the lists
print("List after adding multiple elements:")
print(list1)                 #[5, 12, 43, 56, 78]
print(list2)                 #[1, 45, 67, 3, 30, 41, 0]


# Accessing elements from a tuple

# Creating tuples
tuple1 = (45,54,67,34,21)
tuple2 = ([12,23,4],[1,2,3],"Debashish")

# Accessing elements from tuple (index should be in range)
print(tuple1[0])    #45
print(tuple1[4])    #21

print(tuple2[0][1])     #23
print(tuple2[2][0])     # D



#Deleting different dictionary elements

#Creating dictionary
Dict = {1:"Debashish", 2:"Arun", 3:"Arya", 4:"Deepak"}
print("Dictionary initially: ",Dict)
#element to delete
d = int(input("Enter key to delete:"))

#Deleting element from dictionary
for key in list(Dict): 
    if key == d:  
        del Dict[key] 

print("Dictionary after deletion: ", Dict)