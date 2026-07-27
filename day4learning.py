# type conversion
# a=2
# b=3
# sum=a+b
# print(sum) #implicitly
 
  
# a=2
# b=4
# c=a+b
# print(float(c)) #explicit conversion 

# wap to write string in multiple lines 
# info="""hello my self khushi 
#  am from haryana 
# i am lerning pyhton programming language"""
# print(info)  ### triple quotes are used to write string in multiple lines


#some operation in string
# 1 concatenation
# str1="hello"
# str2="world"
# str3=str1+str2
# print(str3)  #concatenation of two string
 
#if we want to add space between two string then we can use space in between two string
# str1="hello"
# str2="world"
# str3=str1+" "+str2
# print(str3)  #concatenation of two string with space in between


#wap to find the lenght of string
# str1="hello world"
# len=len(str1)
# print("the length of string is :",len) #length of string

# #wap to find the index of string
# str1="khushi verma"
# index=str1[3]
# print("the index of string is :",index) #index of string")


# #wap to find the  slicing of string # this is normal slicing

# str1="khushi verma"
# slicing=str1[3:6]
# print("the slicing of string is:",slicing) #slicing of string

# types of slicing
# 1 reverse slicing
# str1="khshi verma"
# reverse=str1[:: -1]
# print("the reverse of string is:",reverse) #reverse slicing of   full string


#if i want ot reverse some part of string
# str="khushi verma"
# result=str[5:3:-1]
# print(result)

#chatgtp questons
# str1= "programming"
# result=str1[6:2:-1]  #i want reverse the some part of string which is gram
# print(result)

#reverse the string "123456789"
# str1="123456789"
# result=str1[7:0:-2]  # i want to reverse some part of string 8642
# print(result)

#reverse the string
# str1="nohtyp"
# result=str1[::-1]
# print(result)


# #reverse the string
# str1="i love python language"
# result=str1[12:7:-1]
# print(result)

# #negative indexing
# str1="apple"
# result=str1[-4:-1] # if we write -1 in negative indexing then it will not include the last index 
# print(result)  #  

# # second type of negative indexing
# str1=" india is great "
# result=str1[-6:-1]
# print(result) 


# #pura end to end ka negative indexing
# str1="pyhton is amazing for coding"
# result=str1[-18:]
# print(result)

#lower case and upper case
# str1="hello world"
# result=str1.upper() #upper case
# print(result)

# str1="HELLO WORLD"
# result=str1.lower() #lower case
# print(result)

# #endwith and startnwith
# str1="python is programming language"
# result=str1.startswith("python") #startwith
# print(result)
# str2="python is programming language"
# result=str2.endswith("language") #endwith
# print(result)



#capatlize and title
str1="python is amazing programming language"
result=str1.capitalize() #capitalize starting letter will be capital
print(result)

str1="python is amazing programming language"
result=str1.title() #title all satarting letter of each word will be capital
print(result)


#replace and count
str1="i love python programming language"
result=str1.replace("python","java")
print(result) #replace python with java

str1="i love python programming language"
result=str1.count("programming")
print(result) #count the number of occurence of programming in string

#find and index

str1="python is programming language"
result=str1.find("programming")
print(result) #find the index of programming in string agr isko jo word dhund rhe wo nahi milta toh ye -1 return krta h ye indexing ki trh h bs indexing m error ajata h agr vale nahi milti toh
#hum indexing bhi ka kr k dekh lete hei
str1="python is programming language"
result=str1.index("programming")
print(result)  #index the index of programming in string agr isko jo word dhund rhe wo nahi milta toh ye error ajata h ye find ki trh h bs find m -1 return krta h agr vale nahi milti toh


#isalnum and isalpha
str1="pythoon234"
result=str1.isalnum() #isalnum means to find there is any alphanumeric character in string or not 
print(result)

str1="python"
result=str1.isalpha() #isalpha means to find ther is any alphabetic character in string or not
print(result)


#islower and isupper
str1="python"
result=str1.islower() #islower means to find there is any lower case character in string or not
print(result)

str1="PYTHON"
result=str1.isupper() #isupper means to find there is any upper case character in string or not
print(result)

#isspace and printable
str1="  "
result=str1.isspace() #isspace means to find there is any space character in string or not
print(result)

#printable
str1="python is programming language"
result=str1.isprintable() #isprintable means to find there is any printable character in string or not
print(result)

#not printable
str1="python is programming language\n"
result=str1.isprintable() #isprintable means to find there is any printable character in string or not
print(result)


#istile and isdigit
str1="python is programming language"
result=str1.istitle() #istile means to finf there is any  title character in string or not
print(result)

str1="12345"
result=str1.isdigit() #isdigit means to find there is any digit character in string or not
print(result)

#swapcase and zfill
str1="python is programming language"
result=str1.swapcase() #swapcase means to swap the case of character in string
print(result)

number="5"
result=number.zfill(3) #zfill means 3 isliye h kyuki humne 3 likha h isme 5 ko 3 digit me convert krna h toh ye 005 return krega
print(result)