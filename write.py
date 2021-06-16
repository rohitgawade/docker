file1 =open("C:/Users/rohit/Documents/abcd.txt",'r')
file2 =open("C:/Users/rohit/Documents/abcd1.txt",'w')
data=file1.read()
file2.write(data)
print(data)

