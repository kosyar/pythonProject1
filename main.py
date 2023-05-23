# Функция для получения месяца из названия файла
def get_month(filename):
    month = filename.split('_')[-1].split('.')[0]
    return month

# Чтение списка чеков из файла
with open('чеки.txt', 'r') as file:
    check_list = file.read().splitlines()

# Создание словаря для хранения чеков по месяцам
check_dict = {}

# Создание словаря для хранения оплаченных услуг по месяцам
paid_services = {}

# Перебор чеков и распределение по месяцам
for check in check_list:
    month = get_month(check)
    if month not in check_dict:
        check_dict[month] = []
    check_dict[month].append(check)

# Сортировка чеков в каждом месяце
for month in check_dict:
    check_dict[month].sort()

# Запись чеков в папки и формирование списка оплаченных услуг
output_lines = []
not_paid_services = {}

for month in check_dict:
    output_lines.append(f'/{month}:')
    paid_services[month] = set()
    for check in check_dict[month]:
        output_lines.append(f'/{month}/{check}')
        service = check.split('_')[0]
        paid_services[month].add(service)

# Формирование списка неоплаченных услуг
not_paid_lines = ['не оплачены:']
for month in paid_services:
    not_paid_services[month] = set()
    for service in paid_services[month]:
        if service not in paid_services:
            not_paid_services[month].add(service)

# Запись результатов в файл
with open('чеки_по_папкам.txt', 'w') as file:
    file.write('\n'.join(output_lines + not_paid_lines))

# Формирование списка услуг, которые не были оплачены в каком-либо месяце
services_not_paid = set()
for month in not_paid_services:
    services_not_paid.update(not_paid_services[month])

# Вывод списка услуг, которые не были оплачены
print("Список неоплаченных услуг:")
for service in services_not_paid:
    print(service)