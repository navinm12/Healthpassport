from .models import user
from .models import doctor
from .models import patient
from .models import medicals



def User_state_creation(user_email,user_name,user_type):
    
    user.email=user_email
    user.name=user_name
    user.user_type=user_type
    return 'created successfully'

def get_state_user():
    users=[]
    users.append(user.email)
    users.append(user.name)
    # users.append(user.eth_address)
    users.append(user.user_type)
    return users




def doctor_state_creation(doctor_email,doctor_name,doctor_hospital_name,doctor_eth_address,doctor_type):
    doctor.email=doctor_email
    doctor.name=doctor_name
    doctor.hospital_name=doctor_hospital_name
    doctor.eth_address=doctor_eth_address
    doctor.doctor_type=doctor_type
    return 'created successfully'

def get_state_doctor():
    doctors=[]
    doctors.append(doctor.email)
    doctors.append(doctor.name)
    doctors.append(doctor.hospital_name)
    doctors.append(doctor.eth_address)
    doctors.append(doctor.doctor_type)
    return doctors

def Patient_state_creation(patient_email,patient_ethaddress,patient_name,patient_number):
    patient.email=patient_email
    patient.ethaddress=patient_ethaddress
    patient.name=patient_name
    patient.number=patient_number
    return 'created successfully'

def get_state_patient():
    patients=[]
    patients.append(patient.email)
    patients.append(patient.ethaddress)
    patients.append(patient.name)
    patients.append(patient.number)
    return patients


def Medical_state_creation(email,medname,ownername):
    
    medicals.email=email
    medicals.medname=medname
    medicals.ownername=ownername
    return 'created successfully'

def get_state_Medical():
    medicalshop=[]
    medicalshop.append(medicals.email)
    medicalshop.append(medicals.medname)
    medicalshop.append(medicals.ownername)
    return medicalshop
