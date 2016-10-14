### Import Excel file with Pandas

xls_file = pd.ExcelFile('path')
sheets = xls_file.sheet_names
df = xls_file.parse(sheets[0])


### Transform double index in 2 variables

table["var1"] = (table.index.levels[0])[table.index.labels[0]]
table["var2"] = (table.index.levels[1])[table.index.labels[1]]
