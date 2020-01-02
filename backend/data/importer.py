# Reading an excel file using Python
import xlrd
import datetime
from news import News


def read_excel():
    loc = ("1.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    news = []
    for i in range(1, sheet.nrows):
        news.append(News(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(
            i, 2), sheet.cell_value(i, 3), sheet.cell_value(i, 4), sheet.cell_value(i, 5)))

    return news


if __name__ == "__main__":
    print(read_excel()[0])
