# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from xlrd import open_workbook
from src.utils.log_util import log
from configure.configure import *


class ExcelReader(object):
    def __init__(self, book, sheet=0):
        """Read workbook
        :param book: 路径
        :param sheet: sheet名字或者index号
        """
        self.book_name = book
        self.sheet_locator = sheet

        self.book = open_workbook(self.book_name)
        self.sheet = self._sheet()

    def _sheet(self):
        """Return sheet"""
        if type(self.sheet_locator) == int:
            sheet = self.book.sheet_by_index(self.sheet_locator)  # by index
        elif type(self.sheet_locator) == str:
            sheet = self.book.sheet_by_name(self.sheet_locator)  # by name
        else:
            log.error("file: {0} input wrong sheetname or sheet index".format(self.book_name))
            sheet = None
        return sheet

    @property
    def title(self):
        """First row is title."""
        try:
            return self.sheet.row_values(0)
        except IndexError:
            log.error("This is a empty sheet, please check your file.")

    @property
    def data(self):
        """Return data in specified type:
            [{row1:row2},{row1:row3},{row1:row4}...]
        """
        sheet = self.sheet
        title = self.title
        data = list()

        # zip title and rows
        for col in range(1, sheet.nrows):
            s1 = sheet.row_values(col)
            s2 = [str(s).encode('utf-8') for s in s1]  # utf-8 encoding
            data.append(dict(zip(title, s2)))
        return data

    @property
    def nums(self):
        """Return the number of cases."""
        return len(self.data)


if __name__ == '__main__':
    phone = ExcelReader(baidu_excel, 0)
    print(phone.title)
    # print(phone.data)
    # print([str(i).encode('utf-8') for i in phone.data])
    print([i['keyword'].decode('utf-8') for i in phone.data])
    print(phone.nums)
