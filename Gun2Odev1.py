
# Bir öğrenci kayıt sistemi yazdığımızı düşünelim.

students = ["asu", "betül", "pınar", "eda"]
print(students)

# 1-Aldığı isim soy isim ile listeye öğrenci ekleyen

addStudent = input("Eklemek istediginiz ismi giriniz:")
students.append(addStudent)
print(students)

# 2-Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

clearStudent = input("Cikarmak istediginiz ismi giriniz:")
students.remove(clearStudent)
print(students)

# 3-Listeye birden fazla öğrenci eklemeyi mümkün kılan

def addMultiple():
    sayi = int(input("Kac tane ogrenci eklemek istersiniz?"))
    i = 0
    while i < sayi:
        studentName = input("Eklemek istediginiz ismi giriniz:")
        students.append(studentName)
        i += 1
addMultiple()
print(students)


# 4-Listedeki tüm öğrencileri tek tek ekrana yazdıran

for student in students:
    print(student)

# i = 0
# while i < len(students):
#     print(students[i])
#     i += 1

# 5-Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

for student in students:
    print(f"{student} adli ogrencinin numarasi {students.index(student)}")

# 6-Listeden birden fazla öğrenci silmeyi mümkün kılan 

def clearMultiple():
    sayi = int(input("Kac tane ogrenci cikarmak istersiniz?"))
    i = 0
    while i < sayi:
        studentName = input("Cikarmak istediginiz ismi giriniz:")
        students.remove(studentName)
        i += 1
clearMultiple()
print(students)