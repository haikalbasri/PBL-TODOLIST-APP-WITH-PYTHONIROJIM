#contoh list
students = ["Andi", "Budi", "Caca", "Dedi", "Eka"]
masukan_nama = input("Masukan Nama : ")
students.append(masukan_nama)
students2 = ["Fani", "Gani", "Hani", "Iani", "Jani"]
# untuk menggabungkan 2 buah list  
students.extend(students2) 
for i in range(len(students)): #students:
    print(f"{i+1}. {students[i]}")
print("pilih yang akan dihapus")
input_delete = int(input("Masukan index yang ingin dihapus : "))
for student in students:
    if students.index(student) == input_delete-1:
        students.remove(student)
        break
print(students)