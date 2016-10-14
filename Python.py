### Import Excel file with Pandas

xls_file = pd.ExcelFile('path')
sheets = xls_file.sheet_names
df = xls_file.parse(sheets[0])
