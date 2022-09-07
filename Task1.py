def StringManipulation(str):
    lst=[]
    for i in str:
        if ord(i) in range(65,90) or ord(i) in range(97,120):
            lst.append(chr(ord(i)+1))
        elif ord(i)==90:
            lst.append('A')
        elif ord(i)==122:
            lst.append('a')
        else:
            lst.append(i)
    result1=''.join(lst)

    result2=str[::-1]

    result3= str[::2]
    print("1. ",result1,"\n2. ",result2,"\n3. ",result3)

str=input("Enter a string: ")
result = StringManipulation(str)
print(result)