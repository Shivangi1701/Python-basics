# Python code to demonstrate the working of index() and reverse()
import array

# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 2, 5])

# printing original array 
print ("The new created array is : ",end="") 
for i in range (0,6): 
    print (arr[i],end=" ") 
  
print ("\r") 

# using index() to print index of 1st occurrenece of 2 
print ("The index of 1st occurrence of 2 is : ",end="") 
print (arr.index(2)) ###   GIVES THE POSITION --------------


#using reverse() to reverse the array 
arr.reverse() 

print("The revesed array is : ", end = ' ')
for i in range(0,6):
    print(arr[i], end = ' ')
 
