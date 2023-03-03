import os
import random
os.system("cls")

data = []

for i in range(10):
    a = random.randint(1, 10)
    data.append(a)

# Sorting menggunakan Quick Sort
def quickSort(data):
    if len(data) <=1:
        return data
    else:
        pivot = data[0]
        smaller = [x for x in data[1:] if x <= pivot]
        larger = [x for x in data[1:] if x > pivot]

        return quickSort(smaller) + [pivot] + quickSort(larger)

# Jalannya Program
print(35*"=")
print("Pengurutan Angka dengan Quick Sort")
print(35*"=")
print()

print(f"List sebelum diurutkan = {data}")

# Proses Sorting
result = quickSort(data)

# Hasil Sorting
print(f"List sesudah diurutkan dengan quick sort = {result}")