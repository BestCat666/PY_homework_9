import pandas
import openpyxl

def export_():
    d1 = pandas.read_excel('my_project.xlsx')
    d1 = d1.set_index('ID')
    d1.to_excel('export_file.xlsx')


    

