#num=int(input("Enter a number:"))
#i=1
#while i<=10:
   # print(i,"*",num,"=",i*num)
   # i+=1

#i=1
#while i<=5:
   # print("aish")
   # i+=1

#i=12
#while True:
   #print(i)
    #i+=1

#n =int(input("Enter a number:"))
##i=1
#while i<=n:
    #print(i)
   # i+=1

#n=int(input("Enter a number:"))
#fact=1
#for i in range(1,n+1):
   # fact=fact*i
    #print("Factorial of no:",fact)

# n=int(input("Enter a number:"))
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
#     print("Reverse of a number:",rev)

# n=int(input("Enter a number:"))
# rev=0
# digit=0
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#     print(rev)

# n=int(input("Enter a number:"))
# temp=n
# rev=0
# while n>0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
#     if rev==temp:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

#list

# list=[1,2,3,4,5]
# list1=[1,"Aiswarya",3.4444,True,2,4,5,6]
# list2=[{1,2},{2,3},{23,45}]
# print(list)
# print(list1)
# print(list2)

# print(list[3])#index inside the square brackets
# print(list[-2])#index inside the square brackets

#list slicing
# list=[1,2,3,4,5,6,3,9,0]
# list1=[4,5,6,3,8,6]
# print(list[0:9:2])
# print(list[3:])
# print(list[2::7])
# print("The length of a string",len(list))
# list.append(8)
# print(list)
# list.insert(1,23)
# print(list)
# list.extend([24,25])
# print(list)
# list.remove(2)
# print(list)
# list.pop(1)
# print(list)
# list.clear()
# print(list)
# pos=list.index(4)
# print(pos)
# count=list.count(3)
# print(count)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list2=list+list1
# print(list2)
# list.copy()
# print(list)
# print(list*2)
# print(10 in list)

# fruits=["apple","orange","strawberry"]
# for i in fruits:
#     print(fruits)

# fav_cities=[]
# for i in range(1,5):
#     print("Enter your fav city",i,":")
#     str=input()
#     fav_cities.append(str)
# for i in range(len(fav_cities)-1,-1,-1):
#     print("My favourite city",i,"is",fav_cities[i])

# s=set()
# s1={1,3,5,4}
# s2={6,7,8,9}
# s3={1,"Aiswarya",3.4444,True,2,4,5,6}
# print(s1)
# print(s2)

#set
# fruits={"apple","orange","strawberry"}
# for f in fruits:
#    print(f)
# s1.add(5)
# s1.add(6)
# print(s1)

# A={1,2,3,4,5}
# B={6,7,8,8,0}
# print(A|B)   #{0, 1, 2, 3, 4, 5, 6, 7, 8}
# print(A - B)    #{1, 2, 3, 4, 5}

# print(len(A))
# print(max(A))
# print(min(B))
# print(sum(A))

# print(1 in A)
# print(2 not in B)
# print(5 in A)
# print(99 in B)

#tuple
# t=(2,"hi")
# t1=(7,4,(2,3),6)
# a,b,c=(1,2,3)
# # print(t)
# print(t[0])
# print(t[-2])
# print(t[1:3])
# print(len(t))
# print(t+t1)
# print(t*3)
# count=t.count(2)
# print(count)
# # pos=t.index(3)
# # print(pos)
# print(max(t))
# print(min(t))
# print(sum(t))
# print(a)
# print(10 in t)
# print(type(t1))
# print(5 not in t)
# num,word=t
# print(num)
# print(word)

#dictionary
# d1={}
# d2={"name":"aiswarya","age":20,"city":"coimbatore"}
# d3={"name":"rooga","age":21}
# # print(d3)
# print(d3["age"])
# d3["name"]="sree"
# print(d3)
   # d3=dict(id=103,branch="CSE")
# print(d3)
# del d2["age"]
# print(d2)

#nested dic
# d4={"student":{"name":"Bob","age":22},"marks":{"math":34,"science":56}}

#string
# text="4567889743"
# print(text)
# print(text[-1])
# print(text[:4])
# print(text[4::2])
# print(text[::-1])
# print(len(text))
# text_lower=text.lower()
# print(text_lower)     #lower
# print(text.capitalize())  #capital 1st letter
# print(text.title())

# print(text.strip()) #space not print
# print(text.split(" "))
# new_text="i have been to lovai lake and tried the jet ski"
# new_list=new_text.split(" ")
# str=",".join(new_list)
# print(str)
# print(text.find("am"))

# print(text.replace("I am from coimbatore","i am from chennai"))
# print(text.isalpha()) #letters t or f
# print(text.isdigit())#digits t or f 

# text="1234568hugj"
# if text.isalpha:
#     print("letters")
# elif text.isdigit:
#     print("digits")
# else:
#     print("None")
    
# def bubble_sort(arr):
#    n=len(arr)
#    for i in range(n-1):
#       swapped=False
#       for j in range(n-1-i):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             swapped=True
#       if not swapped:
#             break
#    return arr

arr=[1,45,3,2,6]
# print(bubble_sort(arr))

# def selection_sort(arr):
#   n=len(arr)
#   for i in range(n-1):
#     min_idx=i
#     for j in range(n-1):
#        if arr[j]<arr[min_idx]:
#           min_idx=j
#    arr[i],arr[min_idx]=arr[min_idx],arr[i]
#   return arr


# def insertion_sort(arr):
#           for i in range(1,len(arr)):
#              key=arr[i]
#              j=i-1
#              while j>=0 and arr[j]>key:
#                 arr[j+1]=arr[j]
#                 j-=1
#                arr[j+1]=key
#              return arr
          
def merge_sort(arr):
    if len(arr)>=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend







    
