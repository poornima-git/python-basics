class Instructor:
    def __init__(self, inst_name, address):
        self.name = inst_name
        self.address = address
        
instructor_1 = Instructor("sona", 'mumbai')
instructor_2 = Instructor("keerthy","delhi" )
instructor_3 = Instructor("raj", "pune")
print(instructor_1.name)
print(instructor_1.address)
print(instructor_2.name)
print(instructor_2.address)
print(instructor_3.name)
print(instructor_3.address)