class PatientRecord:
    def __init__(self, name, age, medical_id, address):
        self.name = name
        self.age = age
        self.medical_id = medical_id
        self.address = address
    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Medical ID: {self.medical_id}, Address: {self.address}"
class IndexBlock:
    def __init__(self):
        self.pointers = []
    def add_pointer(self, block_index):
        self.pointers.append(block_index)
class IndexedFileAllocation:
    def __init__(self, block_size=1):
        self.disk = []  # Simulate disk blocks
        self.index_table = {}
        self.block_size = block_size
    def add_patient(self, patient):
        if patient.medical_id in self.index_table:
            print(f"Patient with Medical ID {patient.medical_id} already exists.")
            return
        index_block = IndexBlock()
        self.disk.append(patient)  # Add the patient record to the disk
        index_block.add_pointer(len(self.disk) - 1)  # Point to the block where the patient record is stored
        self.index_table[patient.medical_id] = index_block
        print(f"Added: {patient}")
    def delete_patient(self, medical_id):
        if medical_id not in self.index_table:
            print(f"Patient with Medical ID {medical_id} not found.")
            return
        index_block = self.index_table[medical_id]
        for block_index in index_block.pointers:
            self.disk[block_index] = None  # Mark the block as deleted
        del self.index_table[medical_id]
        print(f"Deleted patient with Medical ID: {medical_id}")
    def update_patient(self, medical_id, updated_patient):
        if medical_id not in self.index_table:
            print(f"Patient with Medical ID {medical_id} not found.")
            return
        index_block = self.index_table[medical_id]
        block_index = index_block.pointers[0]  # Assuming there's only one block for each patient
        self.disk[block_index] = updated_patient  # Update the patient record
        print(f"Updated patient with Medical ID: {medical_id} to {updated_patient}")
    def retrieve_patient(self, medical_id):
        if medical_id not in self.index_table:
            print(f"Patient with Medical ID {medical_id} not found.")
            return None
        index_block = self.index_table[medical_id]
        block_index = index_block.pointers[0]
        patient_record = self.disk[block_index]
        print(f"Retrieved: {patient_record}")
        return patient_record
    def display_patients(self):
        print("Current Patient Records:")
        for record in self.disk:
            if record:
                print(record)
    def calculate_disk_space(self):
        total_space = len(self.disk) * self.block_size
        used_space = sum(1 for record in self.disk if record is not None) * self.block_size
        print(f"Total Disk Space: {total_space} units")
        print(f"Used Disk Space: {used_space} units")
        print(f"Free Disk Space: {total_space - used_space} units")
emr_system = IndexedFileAllocation()
patient_a = PatientRecord("John Smith", 45, 1001, "123 Hospital Road")
patient_b = PatientRecord("Jane Doe", 32, 1002, "456 Clinic Avenue")
patient_c = PatientRecord("Michael Johnson", 58, 1003, "789 Medical Plaza")
emr_system.add_patient(patient_a)
emr_system.add_patient(patient_b)
emr_system.add_patient(patient_c)
emr_system.display_patients()
emr_system.retrieve_patient(1001)
patient_a_updated = PatientRecord("John Smith", 45, 1001, "321 Hospital Road")
emr_system.update_patient(1001, patient_a_updated)
emr_system.display_patients()
emr_system.delete_patient(1002)
emr_system.display_patients()
emr_system.calculate_disk_space()
