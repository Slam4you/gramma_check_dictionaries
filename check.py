check_list = []
errors_list = []
for i in range(int(input("Введите кол-во слов которые хотите задать для проверки, после введите их"))):
    string = input().lower().split()
    for i in string:
        check_list.append(i)
print(check_list)

for i in range(int(input("Введите кол-во строк которые хотите проверить, после введите их"))):
    string = input().lower().split()
    for i in string:
        if i not in check_list and i not in errors_list:
            errors_list.append(i)

print(*errors_list, sep='\n')