## -*- coding: utf-8 -*-
import os
import calendar
import locale
import shutil

#всякие переменные
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
pay_list = {}
services = ['газоснабжение','гвс','теплоснабжение','xвс','электроснабжение']
month_name_list = {}

#получаем месяцы из системы
def month_name():
    month_name = []
    for name in calendar.month_name:

        month_name.append((name.capitalize()))
    return month_name
month_name_list = month_name()
month_name_list = month_name_list[1:]
month_name_list = [x.lower() for x in month_name_list]

#делаем лист на весь год чтобы было не оплачено
def gen_pay_list():
    for i in range(len(month_name_list)):
        for j in range(len(services)):
            pay_list[str(month_name_list[i]) + str([services[j]])] = ["0"]


gen_pay_list()

#читаем чеки из файла. можно потом переделать на лист файлов из директории
def read_file(file_name):
    file = open(file_name, 'r',encoding="utf-8")
    lines = file.readlines()
    file.close()
    return lines
check = read_file("чеки.txt")

#print(check)
#check directory is exist or not created


def file_move(check,file_name_src,file_name_dest):
    if not os.path.isdir(check):
        os.mkdir(check)
    else:
        #get directory address
        check_dir = os.path.abspath(check)
        check_dir = os.path.dirname(check_dir)
        check_dir = os.path.abspath(check_dir)
        #check file is exist
        file_name_src = './' + file_name_src
        path = './гвс_февраль.pdf'
        print("@@@@@@@@@@@@@@@@@@@@")
        print(str(file_name_src))
        print(os.path.isfile(str(file_name_src)))
        print(str(file_name_dest))
        print("@@@@@@@@@@@@@@@@@@@@")

        file_name_dest = check_dir + "\\" + file_name_dest
        #print("file to " + file_name_src + " to " + file_name_dest)
        print(type(file_name_src))
        print(os.path.isfile(file_name_src))

        print(os.path.isfile(path))
        print(type(path))
        if os.path.isfile(str(file_name_src)):
            print("copy file" + file_name_src + " to " + file_name_dest)
            print("111")
            #shutil.move(file_name_src, file_name_dest)
            print("222")
        #else:
            #print(file_name_src + " is not exist")
        '''
        try:
            shutil.move(check_dir + "\\" + file_name_src, check_dir + "\\" +check + "\\" + file_name_dest)
            print("all good")
        except shutil.Error as e:
            print('Error: %s' % e)
            #print("no files")
            print(check_dir + "\\" + file_name_src, check_dir + "\\" +check + "\\" + file_name_dest)
        #print("all good")
'''

#создаём масив для проверок оплат
def get_month_list(file_list):
    month_list = []
    month_services= []
    for i in range(len(file_list)):
        test3 = file_list[i].replace(".","_")
        month_list.append(test3.split("_")[1])
        month_services.append(test3.split("_")[0])
    return month_list,month_services

check = get_month_list(check)



#устанавливая за что заплачено а за что не оплачено
def main_logig(checks):
    lens = len(checks[0])
    for i in range(lens):
        dict = {}
        dict[checks[1][i]]= checks[0][i]
        for des in range(lens):
            param = "1"
            services = checks[1][des]
            pay_list[str(checks[0][des]) + str([services])] = [param]
main_logig(check)

#обернут в процедуру и добавить перенос файлов по папкам

old = ""
file = open("output.txt", "w", encoding="utf-8")
file.write("не оплачены: " + "\n")
#print(type(pay_list))

for parameter in pay_list:
    strs = parameter.replace("['", "_")
    strs2 = strs.replace("']", "_")
    strs2 = strs2.split("_")
    if pay_list.get(parameter) != ['1']:
            if old != strs2[0]:
                old = strs2[0]
                #print(old + ":")
                file.write(old + ":" + "\n")
                file.write(strs2[1] + "\n")
                #print(strs2[1] + "_"+strs2[0] + ".pdf")
                print("################################")
                string_to_write_file = strs2[1] + "_"+strs2[0] + ".pdf"
                print(string_to_write_file)
                string_to_read_file =strs2[0] + "_" + strs2[1] + ".pdf"
                print(string_to_read_file)
                print("################################")
                file_move(strs2[0],string_to_read_file,string_to_write_file)
            else:
                file.write(strs2[1] + "\n")
               #print(strs2[1])
'''
    else:
        print(f"Параметр {parameter}  оплачено")
        '''
file.close()
#file output is text file




