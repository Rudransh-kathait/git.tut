
# v2
def greet(name,dept):
    print(f"hi {name}")
    print(f"are you from {dept}")   #POSITIONAL ARGUMENT

greet("rudi"," uk")


def greet(name,dept):
    print(f"hi {name}")
    print(f"are you from {dept}")

greet(dept=" uk",name="rudi")#KEYWORD ARGUMENR



#DEFAULT ARGUMENT
def greet(name,subject,dept="dehradun"):
    print(f"hi {name}")
    print(f"you read {subject}?")
    print(f"are you from {dept}")

greet("rudi","maths")


#ARBITARY ARGUMENT(VARIABLE LENGHT ARGUMENT)
def add(*number):
    c=0
    for i in number:
        c+=i
    print(f"sum is {c}")
add(5,6,7)
