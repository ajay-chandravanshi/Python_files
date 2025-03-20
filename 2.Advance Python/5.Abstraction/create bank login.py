
from abc import ABC,abstractmethod

class Bank(ABC):
    def registration(self):
      print("Registration page")

    def logout(self):
        print("Logout-page")

    @abstractmethod
    def authentication(self):
       pass
    def dashboard(Self):
       print("from Dashboard")
class WebApp(Bank):
   def login(self,id,pass1):
      self.id=id
      self.pass1=pass1
   def authentication(self):
      print("Authentication done")
obj=WebApp()
obj.dashboard()
obj.login(101,123)           
