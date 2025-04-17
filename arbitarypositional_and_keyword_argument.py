# v4

# def add(*numbers):
#     c=0
#     for i in numbers:
#         c+=i
#     print(f"sum is {c}")

# # add(1,2)
# add(6,5,6)

# def add(*numbers,name):
#     c=0
#     for i in numbers:
#         c+=i
#     print(f"sum is {c}")
#     # print(name)
# add(1,2,name="rudi")



# ARBITARY KEYWORD ARGUMENT
def info_persn(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_persn(name="ram",age=30,dept="cse")
info_persn(name="shyam",dept="cse")



# both together

def info_persn(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)    
info_persn(1,2,name="ram",age=30,dept="cse")
info_persn(1,2,3,name="shyam",dept="cse")
