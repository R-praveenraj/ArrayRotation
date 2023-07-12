#Given an integer array A of size N and an integer B, 
#you have to return the same array after rotating it B times towards the right.


def Arrayrotation(array,i,j):
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1

array = [1, 2, 3, 4,5]
k = 2
size=len(array)
if k>size:
    k=k%size

Arrayrotation(array,0,size-1)
Arrayrotation(array,0,k-1)
Arrayrotation(array,k,size-1)
print(array)
