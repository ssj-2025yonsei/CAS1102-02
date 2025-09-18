class A:


    def hello(self):
        print('Hello from A')


class B(A):


    def hello(self):
        print('Hello from B')
        super().hello()


class C(A):


    def hello(self):
        print('Hello from C')
        super().hello()


class D(B, C):


    def hello(self):
        print('Hello from D')
        super().hello()


class E(C):  # Task 1


    def hello(self): pass
        # print('Hello from E')
        # super().hello()


class F(B, E):


    def hello(self): pass
        # print('Hello from F')
        # super().hello()


print(F.mro())  # Task 2


# Task 3
class G(A, B, C, D, E, F):  # This makes an Mro error.


    def hello(self): pass
        # print('Hello from G')
        # super().hello()