#finding maximum
# def find_max(arr):
#     result = arr[0]
#     for x in arr:
#         if x>result:
#             result=x
#     return result
# print(find_max([3,7,2,9,1]))

#Sum of array
# def sum_array(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total
# print(sum_array([1,2,3,4,5]))

#reverse an array 
# def reverse_array(arr):
#     result=[]
#     for x in range(len(arr)-1,-1,-1):
#         result.append(arr[x])
#     return result
# print(reverse_array([1,2,3,4,5,]))

#find second largest
# def find_second_largest(arr):
#     first =second=float('-inf')
#     for x in arr:
#         if x>first:
#             second=first=x
#         elif first>x>second:
#             second=x
#     return second
# print(find_second_largest([3,6,7,2,8]))

#remove duplicates from array 
# def remove_duplicates(arr):
#     seen=set()
#     result=[]
#     for x in arr:
#         if x not in seen:
#             seen.add(x)
#             result.append(x)
#     return result
# print(remove_duplicates([1,2,3,3,4,5,5,6,7,8,9]))

#rotate array
# def rotate_array(arr, k):
#     n = len(arr)
#     k = k % n
#     rotated = arr[n-k:] + arr[:n-k]
#     return rotated
# print(rotate_array([1, 2, 3, 4, 5], 3))

#merge two sorted arrays
# def merge_sorted_arrays(arr1,arr2):
#     i,j,result=0,0,[]
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<=arr2[j]:
#             result.append(arr1[i]);i+=1
#         else:
#             result.append(arr2[j]);j+=1
#     result.extend(arr1[i:])
#     result.extend(arr2[j:])
#     return result
# print(merge_sorted_arrays([1,3,5],[2,4,6]))

# #find missing numbers
# def find_missing_number(arr,n):
#     expected_sum=n*(n+1)//2
#     return expected_sum-sum(arr)
# print(find_missing_number([1,2,4,5],3))

#two sum problem 
# def two_sum(arr,target):
#     seen={}
#     for i,num in enumerate(arr):
#         complement =target-num
#         if complement in seen:
#             return[seen[complement],i]
#         seen[num]=i
#     return None
# print(two_sum([1,2,3],5))

#Move Zeros to end
# def move_zeros_to_end(arr):
#     result=[x for x in arr if x !=0]
#     result.extend([0]*(len(arr)-len(result)))
#     return result
# print(move_zeros_to_end([0,1,0,3,12]))

#count characters
# def count_characters(text):
#     counts={}
#     for ch in text:
#         counts[ch]=counts.get(ch,0)+1
#     return counts
# print(count_characters("hello"))

# #check anagram 
# def is_anagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     return count_characters(str1)==count_characters(str2)
# print(is_anagram("listen","silent"))

#longest word
# def longest_word(text):
#     words=text.split()
#     longest=''
#     for w in words:
#         if len(w)>len(longest):
#             longest=w
#     return longest
# print(longest_word("python is awesome"))

#count vowels and consonants
# def count_vowels_consonants(text):
#     vowels=set('aeiouAEIOU')
#     v=c=0
#     for ch in text:
#         if ch.isalpha():
#             if ch in vowels: v+=1
#             else:c+=1
#         return(v,c)
# print(count_vowels_consonants("HELLO World"))

#remove spaces
# def remove_spaces(text):
#     result=''
#     for ch in text:
#         if ch!=' ':
#             result+=ch
#     return result
# print(remove_spaces("hello world python"))



     


