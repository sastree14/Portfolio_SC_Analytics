from openpyxl import Workbook
def export_schedule(rows,path):
    wb=Workbook(); ws=wb.active; ws.append(["month","payment","interest","principal","balance"])
    for row in rows: ws.append(row)
    wb.save(path)
