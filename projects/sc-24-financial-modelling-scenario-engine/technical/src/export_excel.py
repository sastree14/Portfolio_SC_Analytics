from openpyxl import Workbook

def export(rows,path):
    wb=Workbook(); ws=wb.active; ws.append(["month","revenue","fcf","cash"])
    for row in rows: ws.append([row["month"],row["revenue"],row["fcf"],row["cash"]])
    wb.save(path)
