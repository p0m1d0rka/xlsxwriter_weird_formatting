import xlsxwriter
import xlsxwriter
import os
filename = 'xlsxwriter_test_python' + os.environ['PYTHON_VERSION'] + '.xlsx'

workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()
big_numbers_format = workbook.add_format({'num_format': '# ##0'})
percent_format = workbook.add_format({'num_format': '0,00%'})

#expected in excel 100 000 000, got 100000 000
worksheet.write_number  (0, 0, 100000000, big_numbers_format)

#expected 99,99% in excel got 100%
worksheet.write_number  (0, 1, 0.9999, percent_format)

workbook.close()


