# nums = [10, 25, 30, 45, 50, 60]
# res={i for i in nums if i%5==0 and i%10!=0}
# print(res)

# num=[12,34,5]
# sum=0
# total=0
# for i in num:
#     digit=i%10
#     res=i//10
#     sum=digit+res
#     total=total+sum
# print(total)

# num=[12,34,5]
# total=0
# for i in num:
#     digit_sum=sum(int(d) for d in str(i))
#     total+=digit_sum
# print(total) 

# def recursive_digit_sum(n):
#     if n == 0:
#         return 0
#     return n % 10 + recursive_digit_sum(n // 10)

# num = [12, 34, 5]
# total = sum(recursive_digit_sum(i) for i in num)
# print(total)
   

# num=[1,2,3]
# n=2
# result=num*2
# print(result)

# num=[1,2,3]
# n=2
# res=[]
# for i in range(n):
#     res.extend(num)
# print(res)

# from collections import Counter
# nums = [10, 25, 30, 45, 50, 60]
# res=Counter(nums)
# print(dict(res))
    
# def count_freq(list):
#     freq={}
#     for i in list:
#         if i in freq:

#             freq[i]+=1
#         else:

#             freq[i]=1
#     return freq     
# print(count_freq([10, 25, 30, 45, 50, 60, 10, 30, 25]))


# count=0
# for i in range(2,20):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
         
#     if is_prime:
#         count+=1           
# print(count)                
            
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         for j in range(2,i):
#             if n % i == 0:
#                 return False
#     return True

# def count_primes(start, end):
#     count = 0
#     for i in range(start, end + 1):
#         if is_prime(i):
#             count += 1
#     return count

# print(count_primes(10, 50))  

# n=9875
# while n>=10:
#     n=sum(int(digit) for digit in str(n))
# print(n)    

# def sum_single_digit(n):
#     while n >=10:
#        n=sum(int(i) for i in str(n))
#     return n
# print(sum_single_digit(9875))   

     


   