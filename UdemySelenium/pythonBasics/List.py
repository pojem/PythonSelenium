a,b,c = 5, 6.4, "great"
print("{} {}".format("value is", c))
print(type(a))
print(type(b))
print(type(c))
aa ="hahah"

bb ="jojo"

cc = aa + bb

print(cc)

list = [aa, bb, 2, 3, "sss"]

print(list[1])
print(list[-1]) #-1 last index in list
print(list[1:3])

list.insert(3,"marko") # update list

print(list)

list[2] = "jabuk"
print(list)

del list[0] # delete element from list
print(list)
