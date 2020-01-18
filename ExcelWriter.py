import openpyxl as op

col1 = "Apples"
col2 = "2"
wb = op.load_workbook("file.xlsx")
ws = wb.active
print(ws)
ws.append([col1, col2])
wb.save("file.xlsx")
wb.close()
