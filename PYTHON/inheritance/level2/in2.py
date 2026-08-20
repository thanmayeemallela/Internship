class CPU:
    def process(self):
        print("CPU is processing")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cpu.process()
        print("Computer is running")

Computer().run()
