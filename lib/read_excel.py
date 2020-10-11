import xlrd
from config.config import *

def read_excel_data(data_file,sheet_name):
    data_list = []
    excel_path = xlrd.open_workbook(os.path.join(test_data_file,data_file))
    excel_sheet = excel_path.sheet_by_name(sheet_name)
    for i in range(1,excel_sheet.nrows):
        data = dict(zip(excel_sheet.row_values(0),excel_sheet.row_values(i)))
        data_list.append(data)
        return data_list

def get_test_data(case_name,data_list):
    for case_data in data_list:
        if case_name == case_data["case_name"]:
                return case_data

# if __name__ == "__main__":
#     data_list = read_excel_data("test_user_data.xlsx","TestUserLogin")
#     case_data = get_test_data("test_user_login_normal",data_list)
#     print(case_data)