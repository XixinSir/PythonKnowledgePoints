import xlrd

data = xlrd.open_workbook("BURN IN  Condition.xlsx")
table = data.sheet_by_index(1)
totalrow = table.nrows
totalcol = table.ncols
print("总的行数为:%d,总的列数为:%d"%(totalrow, totalcol))