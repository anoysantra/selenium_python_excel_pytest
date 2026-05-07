import openpyxl as excel
#from openpyxl import Workbook
import os


def get_credentials_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Join that directory with your file name
    file_path = os.path.join(current_dir, "creds_test_data.xlsx")
    #file_path = "excel_selenium_pytest/creds_test_data.xlsx"
    wb = excel.load_workbook(file_path)
    sheet = wb["sauce_demo_new"]
    creds_data = []
    for row in sheet.iter_rows(min_row = 2, values_only = True):
        creds_data.append(row)
    return creds_data

if __name__ == "__main__":
    data = get_credentials_data()
    print(data)
    print(type(data))

