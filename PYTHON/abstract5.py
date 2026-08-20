from abc import ABC , abstractmethod
class database(ABC):
    def connect(self):
        pass;
class mysqldb (database):
    def connect(self):
        print("mysql db implementation")
class postegralsqldb(database):
    def connect(self):
        print("postegralsql implementation")
m=mysqldb();
p=postegralsqldb();
m.connect();
p.connect();