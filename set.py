# j=int(input())
# if j>0:
#     data=j//365
#     print(data,"year(s)")
#     j%=365
# if j>0:
#     data1=j//30
#     print(data1,"month(s)")    
#     j%=30
# if j>0:
#     data2=j//7
#     if data2>0:
#         print(data2,"week(s)")
#         j%=7
#     if j>0:
#         print(j,"day(s)")     

# j={1,2,3,4,5}
# j.add(6)
# j.add(7)
# print(j)
# j.update({6,7})
# print(j)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# res=a.symmetric_difference(b)
# print(res)
# res=b.symmetric_difference(a)
# print(res)

# j={5,8,12,3,15,7}
# j.discard(10)
# print(j)
# res=max(j)
# print(res)
# res=min(j)
# print(res)
# res=sum(j)
# print(res)

# j={10, 20, 30, 40}
# j.add(50)
# print(j)

# j={40, 10, 50, 20, 30}
# j.remove(50)
# print(j)

# j=set({15, 20, 25, 30, 35})
# j.discard(25)
# print(j)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# res=A|B
# print(res)
# res=A.union(B)
# print(res)

# A = {10, 20, 30, 40}

# B = {30, 40, 50, 60} 
# res=A&B
# print(res)
# res=A.intersection(B)
# print(res)
# res=A.copy()
# print(res)
# print(len(A))

# j="mahalakshmi"
# k=3
# k=k%len(j)
# print(j[-k:]+j[:-k])

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

# num=[1,2,3]
# n=2
# result=num*2
# print(result)

# from collections import Counter
# nums = [10, 25, 30, 45, 50, 60]
# res=Counter(nums)
# print(dict(res))
    
def count_freq(list):
    freq={}
    for i in list:
        if i in freq:

            freq[i]+=1
        else:
            freq[i]=1
    return freq     
print(count_freq([10, 25, 30, 45, 50, 60, 10, 30, 25]))       


   