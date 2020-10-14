
ItemsinCart = 0
#2 items will be added to cart

#if ItemsinCart !=2:
#    raise Exception("Products Cart count not matching")

if ItemsinCart !=2:
    pass

assert(ItemsinCart == 0)

#try, catch

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print("Some how i reached this block because there is failure it try block")
    print(e)

finally: # this will be always executed no mater if there is exception or not
    print("cleaning up records") # for example delete all the cookies