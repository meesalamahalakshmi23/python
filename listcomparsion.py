1.# list=[[1,2],[3,4],[5,6]]
# res=[ j for i in list for j in i]
# print(res)
    
# res=[]
# for i in list:
#     for j in i:
#         res.append(j)
# print(res)

2.# list=[[2,5],[7,9],[12,15]]
# res=[j for i in list for j in i if j%2==0]
# print(res)

3.# for i in range(1,21):
#     print(i**2)
# res=[i**2 for i in range(1,21)]
# print(res)

4.# for i in range(10,21):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)        

# res=[ i for i in range(10,21) if all(i%j!=0 for j in range(2,i))]        
# print(res)

#7. s=['python','java','c++','developer']
# for i in s:
#     if i in 'python':
#         print(i)

# res=[ i for i in s if i in 'python']
# print(res)

6.# str="mAHAlKSHMI"
# swapped=""
# for ch in str:
#     ascii_val=ord(ch)
#     if 65 <= ascii_val <= 90:        
#         swapped += chr(ascii_val + 32)
#     elif 97 <= ascii_val <= 122:     
#         swapped += chr(ascii_val - 32)
#     else:
#         swapped += ch               

# print(swapped)        

# string into integer 

# s = "4536898365"
# res = 0
# for ch in s:
#     digit = ord(ch) - ord('0')  
#     res = res * 10 + digit
# print(res, type(res))  


# integer into string
# a=10
# s="%a" 
# print(type(s))


# n = 1234
# s = ""
# while n > 0:
#     digit = n % 10
#     s = chr(ord('0') + digit) + s
#     n = n // 10

# print(s, type(s)) 
