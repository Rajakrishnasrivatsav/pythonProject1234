import math
X=5
Y=10
def myfunc():
    global X,Y
    print("Hello",X,Y)
def func():
    print("Welcome",X,Y)
myfunc()
if __name__=="__main__":
    print(__name__)
    print(__file__)
    print(__package__)
    print(dir(math))
    help(math)