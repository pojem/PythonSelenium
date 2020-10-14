str = "RahulShettyAcademy.com"
str1 ="testlab.si"
str2 ="RahulShetty"

print(str[1])  # "a" is output

print(str[0:4]) # if you want to get substring

print(str+str1) #concatenation

print(str2 in str) # returns true

var = str.split(".")
print(var)
print(var[0])

str3 = " great "
print(str3.strip())
print(str3.lstrip()) # right strip
print(str3.rstrip()) # left strip