class program:
    def __int__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(abc):
        print("hello my name is " + abc.name)
        
 p1 = Person("John ", 36)
 p1.myfunc()