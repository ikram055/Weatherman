from sys import argv
import os
from read_data import *
from utils import *

class Weatherman:
    list_of_args = ['-e', '-a','-c']
    if argv[1] in list_of_args:
        try:    
            if argv[1] == '-e':
                year = argv[2]
                path = argv[3]
                directory_path = f'{path}/*{year}*'
                # print(directory_path)
                if os.path.exists(directory_path):
                    data = ReadData()
                    data.calculation(directory_path)
                else:
                    print("Directory doesn't exist!!")
            if argv[1] == '-a':
                year, month = "", "",
                year, month = argv[2].split('/')
                month = utils.get_month_name(int(month))
                path = argv[3]
                directory_path = f"{path}/{path}_{year}_{month}.txt"
                if os.path.exists(directory_path):
                    data = ReadData()
                    data.calculation_for_a(directory_path)
                else:
                    print("Directory doesn't exist!!")
              
            if argv[1]=='-c':
                year, month = "", "",
                year, month = argv[2].split('/')
                month = utils.get_month_name(int(month))
                path = argv[3]
                directory_path = f"{path}/{path}_{year}_{month}.txt"
                if os.path.exists(directory_path):
                    data = ReadData()
                    data.calculation_for_c(directory_path)
                else:
                    print("Directory doesn't exist!!")
                
        except:
            print('Wrong Input!')
    else:
        print("Invalid Arguments!")
    

if __name__ == '__main__':
    Weatherman()