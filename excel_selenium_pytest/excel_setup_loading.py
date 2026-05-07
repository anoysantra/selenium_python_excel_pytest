import openpyxl
from openpyxl import Workbook


#file_path = "/excel_selenium_pytest/creds_test_data.xlsx"

wb = Workbook()
sheet = wb.active
sheet.title = "sauce_demo_new"

creds_data_headers  = ["Username", "Password"]
sheet.append(creds_data_headers)
creds = [
    ["standard_user", "secret_sauce"],
    ["locked_out_user", "secret_sauce"],
    ["problem_user", "secret_sauce"],
    ["performance_glitch_user", "secret_sauce"],
    ["error_user", "secret_sauce"],
    ["visual_user", "secret_sauce"]
]

for cred in creds:
    sheet.append(cred)

wb.save('creds_test_data.xlsx')

print("Credentials data added and file saved successfully!")

#this is a one-time script to create the creds_test_data.xlsx file with the required data for testing. You can run this 
#script once to generate the Excel file, and then use that file in your test scripts to read the credentials data.