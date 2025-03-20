# error in the above code sir ne itna hi karwaya tha
# because humne parent ka use nhi kiya child mai

from abc import ABC,abstractmethod

class A(ABC):
    def new(self):
        print("80%")
    @abstractmethod
    def new1(self):
        pass

class B(A):
    def first(self):
        print("20%")

obj=B()
obj.new()