#！ coding: utf-8
import os,sys
import xlwt
import xlrd
from xlutils.copy import copy

def export_excel(filename,datalist):
	'''
	[A,B]格式
	'''
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('数据')
	header_style = xlwt.XFStyle()

	row = col = 0
	# datalist =  filename.split('\n')
	for item in datalist:
		d = item.split()
		ws.write(row,col,d[col])
		ws.write(row,col+1,d[col+1])
		row += 1
	wb.save(filename)

def filter_ex(filename):
	pass_ex = ['txt']
	if filename.split(".")[1] in pass_ex:
		return True
	else:
		return False

if __name__ == '__main__':
	pwd = os.getcwd()
	cur_name = os.path.basename(__file__) if os.path.basename(__file__) else sys.argv[0]
	filelist = os.listdir(pwd)
	filelist = list(filter(filter_ex,filelist))

	print filelist


	if filelist:
		filelist_abs = [pwd+os.sep+f for f in filelist]
	else:
		filelist_abs =[]

	for file_path in filelist_abs:
		try:
			a_file = open(file_path)
			export_excel(u"数据.xls",a_file.readlines())
		except Exception, e:
			raise
			print "Wrong File:",file_path
		finally:
			a_file.close()