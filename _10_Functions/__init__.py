class A:
    def m1(self):
        print("A m1()")

class B(A):
    def m2(self):
        print("B m2()")

class C(A):
    def m1(self):
        print("c m1()")

class D(B,C):
    pass

d = D()
d.m1()