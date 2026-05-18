import random

patient_name = input('Nhập tên bệnh nhân: ')
patient_gender = input('Nhập giới tính: ')
birth_year = int(input('Nhập năm sinh: '))
phone_num = input('Nhập số điện thoại: ')
email = input('Nhập email: ')
symptom = input('Nhập triệu chứng ban đầu: ')
price = float(input('Nhập chi phí khám: '))

patient_id = f"BN{birth_year}{random.randint(100,999)}"

print('--- THẺ BỆNH NHÂN ---')
print(f'Mã BN: {patient_id}')
print(f'Tên: {patient_name} ({type(patient_name).__name__})')
print(f'Giới tính: {patient_gender} ({type(patient_gender).__name__})')
print(f'Năm sinh: {birth_year} ({type(birth_year).__name__})')
print(f'Điện thoại: {phone_num} ({type(phone_num).__name__})')
print(f'Email: {email} ({type(email).__name__})')
print(f'Triệu chứng: {symptom} ({type(symptom).__name__})')
print(f'Chi phí: {price} VND ({type(price).__name__})')