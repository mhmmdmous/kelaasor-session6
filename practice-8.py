class Hospital:  
    def __init__(self, name, address):  
        self.name = name  
        self.address = address  
        self.doctors_list = []  

    def set_doctors_in_hospital(self, doctor: 'Doctor'):  
        self.doctors_list.append(doctor)  

    def remove_doctors_in_hospital(self, doctor: 'Doctor'):  
        if doctor in self.doctors_list:  
            self.doctors_list.remove(doctor)  

    def get_doctors(self):  
        return self.doctors_list  
    
    def check_doctors(self, doctor):  
        return doctor in self.doctors_list  
        
    def get_doctors_in_degree(self, degree):  
        return [doctor for doctor in self.doctors_list if doctor.degree == degree]  

    def get_doctors_in_doctorate(self, doctorate):  
        return [doctor for doctor in self.doctors_list if doctor.doctorate == doctorate]  


class Doctor:  
    def __init__(self, name, degree, doctorate):  
        self.name = name  
        self.doctorate = doctorate  
        self.degree = degree  
        self.hospitals_list = []  

    def set_hospital(self, hospital: 'Hospital'):  
        self.hospitals_list.append(hospital)  
        hospital.set_doctors_in_hospital(self)  

    def remove_hospital(self, hospital: 'Hospital'):  
        if hospital in self.hospitals_list:  
            self.hospitals_list.remove(hospital)  
            hospital.remove_doctors_in_hospital(self)  

    def get_hospitals(self):  
        return self.hospitals_list
    
# ایجاد یک بیمارستان و دو پزشک  
hospital_1 = Hospital("Bahman Hospital", "iranzamin street")  
doctor1 = Doctor("Dr ali", "omoomi", "doctorian omoomi")  
doctor2 = Doctor("dr sara", "surgeao", "doctorian surgeon")  

# افزودن پزشکان به بیمارستان  
doctor1.set_hospital(hospital_1)  
doctor2.set_hospital(hospital_1)  

# دریافت و چاپ پزشکان بیمارستان  
doctors_in_hospital = hospital_1.get_doctors()  
print(f"doctors in {hospital_1.name}")  
for doctor in doctors_in_hospital:  
    print(f"name: {doctor.name}, degree: {doctor.degree}, doctorian: {doctor.doctorate}")