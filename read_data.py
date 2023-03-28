import glob
import pandas as pd
import math
from termcolor import colored
from utils import *

class ReadData:
    
    def __init__(self):
        self.Max_Temp = math.inf
        self.Min_Temp = -math.inf
        self.Max_Humid = math.inf

        self.Max_Temp_Dict = {}
        self.Min_Temp_Dict = {}
        self.Max_Humid_Dict = {}
        self.list_of_Dict = []
    
    # first use case
    def calculation(self, directory_path):

        for file in glob.glob(directory_path):
            df = pd.read_csv(file, sep=",")
            # Remove the first and last rows
            df = df.iloc[0:-1,[0,1,3,7]]
            # Maximum Temp for each month
            self.Max_Temp = max(df.iloc[:,1])
            self.date = df.iloc[df.iloc[:,1].idxmax(),0]
            self.Max_Temp_Dict[self.date] = self.Max_Temp
            
            # Minimum Temp for each month
            self.Min_Temp = min(df.iloc[:,2])
            self.date_min = df.iloc[df.iloc[:,2].idxmin(),0]
            self.Min_Temp_Dict[self.date_min] = self.Min_Temp

            # Maximum Humidity for each month
            self.Max_Humid = max(df.iloc[:,3])
            self.date_max = df.iloc[df.iloc[:,3].idxmax(),0]
            self.Max_Humid_Dict[self.date_max] = self.Max_Humid
        # print(self.Max_Temp_Dict)
        self.list_of_Dict = [self.Max_Temp_Dict, self.Min_Temp_Dict, self.Max_Humid_Dict]

        output_list = []
        # To Extract Final Temperature
        for i,dic in enumerate(self.list_of_Dict):
            max_temp = None
            max_temp_date = None
            if i==1:
                for date, temp in dic.items():
                    if max_temp is None or temp < max_temp:
                        max_temp = temp
                        max_temp_date = date
            else:
                # Iterate through the dictionary and find the maximum temperature
                for date, temp in dic.items():
                    if max_temp is None or temp > max_temp:
                        max_temp = temp
                        max_temp_date = date

            f_month = utils.get_month_name(int(max_temp_date.split("-")[1]))
            f_date = max_temp_date.split("-")[2]
            output = f"{max_temp}C on {f_month} {f_date}"
            output_list.append(output)

        print("Highest :",output_list[0])
        print("Lowest :",output_list[1])
        print("Humid :",output_list[2])


    #  Second Use Case
    def calculation_for_a(self, directory_path):
        for file in glob.glob(directory_path):
            df = pd.read_csv(file, sep=",")
            # Remove the first and last rows
            df = df.iloc[0:-1,[0,1,3,7]]
            self.Max_Temp = df.iloc[:,1].mean()
            
            # Minimum Average Temp for each month
            self.Min_Temp = df.iloc[:,2].mean()

            # Maximum Average Temp
            self.Max_Humid = df.iloc[:,3].mean()
        print("Highest Average:", str(round(self.Max_Temp))+"C")
        print("Lowest Average:",str(round(self.Min_Temp))+"C")
        print("Humid Average:",str(round(self.Max_Humid))+"C")



    # Third Use Case
    def calculation_for_c(self, directory_path):
        color_temp_max = []
        color_temp_min = []
        for file in glob.glob(directory_path):
            df = pd.read_csv(file, sep=",")
            # Remove the first and last rows
            df = df.iloc[0:-1,[0,1,3,7]]
            for name, series in df.items():
                if name == "Max TemperatureC":
                    for i in series:
                        color_temp_max.append(int(i))
                
                elif name == "Min TemperatureC":
                    for i in series:
                        color_temp_min.append(int(i))
        

        # Print in format
        for i in range(1,len(color_temp_max)):
            print(colored(str(i)+" "+"+"*color_temp_max[i] + str(color_temp_max[i])+'C', "red"))
            print(colored(str(i)+" "+"+"*color_temp_min[i] + str(color_temp_min[i])+'C', "blue"))









    


