import xlsxwriter

def create_xlsx_worksheets(workbook, worksheet_name):
    worksheet = workbook.add_worksheet(name= worksheet_name)
    return worksheet

def format_xlsx_cells(workbook, cell_format):
    formatter = workbook.add_format(cell_format)
    return formatter