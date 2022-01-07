# Write a program to count the number of lines in a file 
fp=open("file.txt","r+")
x = len(fp.readlines())
print(x)