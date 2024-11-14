class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address
    def __repr__(self):
        return f"{self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"
class FileAllocationTable:
    def __init__(self):
        self.table = {}
    def add_record(self, student_id, block_index, length):
        self.table[student_id] = (block_index, length)
    def remove_record(self, student_id):
        if student_id in self.table:
            del self.table[student_id]
    def get_record_location(self, student_id):
        return self.table.get(student_id, None)
class StudentDatabase:
    def __init__(self, block_size=1):
        self.disk = []  
        self.fat = FileAllocationTable()
        self.block_size = block_size
    def add_student(self, student):
        block_index = len(self.disk) // self.block_size
        self.disk.append(student)
        self.fat.add_record(student.student_id, block_index, 1)
        print(f"Added: {student}")
    def delete_student(self, student_id):
        record_location = self.fat.get_record_location(student_id)
        if record_location:
            block_index, _ = record_location
            self.disk[block_index] = None
            self.fat.remove_record(student_id)
            print(f"Deleted student with ID: {student_id}")
        else:
            print(f"Student with ID: {student_id} not found.")
    def update_student(self, student_id, new_student):
        record_location = self.fat.get_record_location(student_id)
        if record_location:
            block_index, _ = record_location
            self.disk[block_index] = new_student
            self.fat.add_record(new_student.student_id, block_index, 1)
            print(f"Updated student with ID: {student_id} to {new_student}")
        else:
            print(f"Student with ID: {student_id} not found.")
    def display_students(self):
        print("Current Student Records:")
        for record in self.disk:
            if record:
                print(record)
    def calculate_disk_space(self):
        total_space = len(self.disk) * self.block_size
        used_space = sum(1 for record in self.disk if record is not None) * self.block_size
        print(f"Total Disk Space: {total_space} units")
        print(f"Used Disk Space: {used_space} units")
        print(f"Free Disk Space: {total_space - used_space} units")
database = StudentDatabase()
student_a = StudentRecord("John Doe", 101, 10, "123 Main Street")
student_b = StudentRecord("Jane Smith", 102, 11, "456 Elm Street")
student_c = StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
database.add_student(student_a)
database.add_student(student_b)
database.add_student(student_c)
database.display_students()
student_a_updated = StudentRecord("John Doe", 101, 10, "321 Main Street")
database.update_student(101, student_a_updated)
database.display_students()
database.delete_student(102)
database.display_students()
database.calculate_disk_space()
