#! /usr/bin/python

class MyClass:
    "Az elso osztaly."
    
    x = 42
    
    def fv(self) : print self.x;
     

mc = MyClass()

print mc.__doc__
# Az elso osztaly.

print mc.x
# 42

mc.fv()
# 42

mc.x = 53
mc2 = MyClass()
mc.fv()
# 53
mc2.fv()
# 42
