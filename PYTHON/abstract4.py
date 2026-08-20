from abc import ABC , abstractmethod
class food(ABC):
    def prepare(self):
        pass;
class pizza (food):
    def prepare(self):
        print("pizza is being prepared")
class burgur (food):
    def prepare(self):
        print("burgur is being prepared")
p=pizza();
b=burgur();
p.prepare();
b.prepare();
