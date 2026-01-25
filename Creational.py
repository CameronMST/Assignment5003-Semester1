CPUInput = input("Enter the CPU Model: ")
GPUInput = input("Enter the GPU Model: ")
MotherboardInput = input("Enter the Motherboard Model: ")
PSUInput = input("Enter the Power Supply Unit Model: ")
StorageInput = input("Enter the Storage Model: ")
MemoryInput = input("Enter the Memory Model: ")
    

class Computer:
    def __init__(self):
        self.CPU = None
        self.GPU = None
        self.Motherboard = None
        self.PSU = None
        self.Storage = None
        self.Memory = None

    def setCPU(self, CPUStyle):
        self.CPU = CPUStyle

    def setGPU(self, GPUStyle):
        self.GPU = GPUStyle

    def setMotherboard(self, MotherboardStyle):
        self.Motherboard = MotherboardStyle

    def setPSU(self, PSUStyle):
        self.PSU = PSUStyle

    def setStorage(self, StorageStyle):
        self.Storage = StorageStyle

    def setMemory(self, MemoryStyle):
        self.Memory = MemoryStyle

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def setCPU(self, CPUStyle):
        self.computer.setCPU(CPUStyle)
        return self

    def setGPU(self, GPUStyle):
        self.computer.setGPU(GPUStyle)
        return self

    def setMotherboard(self, MotherboardStyle):
        self.computer.setMotherboard(MotherboardStyle)
        return self
    
    def setPSU(self, PSUStyle):
        self.computer.setPSU(PSUStyle)
        return self

    def setStorage(self, StorageStyle):
        self.computer.setStorage(StorageStyle)
        return self    

    def setMemory(self, MemoryStyle):
        self.computer.setMemory(MemoryStyle)
        return self
    
    def build(self):
        return self.computer
    

computer = ComputerBuilder() \
            .setCPU(CPUInput) \
            .setGPU(GPUInput) \
            .setMotherboard(MotherboardInput) \
            .setPSU(PSUInput) \
            .setStorage(StorageInput) \
            .setMemory(MemoryInput) \
            .build() #(NeetCode, 2023)
print(f"\nThe Computer has the following specifications:\n{computer.CPU}\n{computer.GPU}\n{computer.Motherboard}\n{computer.PSU}\n{computer.Storage}\n{computer.Memory}\n")


#References

#NeetCode (2023). 8 Design Patterns EVERY Developer Should Know. YouTube. Available at: https://www.youtube.com/watch?v=tAuRQs_d9F8.[Accessed 25/01/2026]