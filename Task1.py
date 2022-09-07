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

    result2=result1[::-1]

    result3= str[::2]
    print("\n1. Succeeding alphabet: ",result1,"\n2. The string is inverted after removing all vowels: ",result2,"\n3. The string has every alternate character from the original string: ",result3)

str=input("Enter a string: ")
result = StringManipulation(str)
print(result)