# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))

#using loops 
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         return fact
# print(factorial(6))

#sum of digits using resursion 
# def sum(n):
#     if n==0:
#         return 0
#     return(n%10)+sum(n//10)
# print(sum(1234))
    
# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(4))

#fib 
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
print(fib(45))








