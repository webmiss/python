# 
# 默认首页
# 

from framework.MySQL import MySQL

class Index:
	def index(self) :
		data = MySQL().find({'table':'cqssc','where':'id=1','field':'id,date'})
		# print(data)
		# rows = MySQL().getRows()
		# print(rows)
		# MySQL().delete('cqssc','id in (1,3)').commit()



		# MySQL().update(
		# 	'cqssc',
		# 	{'date':'','period':'008','num1':'3','num2':'2','num3':'3','num4':'4','num5':'5'},
		# 	'id=1'
		# ).update(
		# 	'cqssc',
		# 	{'date':'','period':'005','num1':'4','num2':'2','num3':'3','num4':'4','num5':'5'},
		# 	'id=2'
		# ).commit()

		# if res==True :
		# 	print(res)
		# else :
		# 	print(res)


