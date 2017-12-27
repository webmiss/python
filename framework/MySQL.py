# 
# MySQL类
# ----------------------------------------------

import mysql.connector
# 配置文件
from app.database import config

class MySQL(object):

	# 构造函数
	def __init__(self):
		# 配置文件
		if config :
			self.config = config
			self.__sql=[]

	# 查询
	def find(self,parm=''):
		# 表
		if 'table' in parm.keys() :
			table = parm['table']
		else:
			print({'state':'n','msg':'请传入表！'}); exit()
		# 字段
		if 'field' in parm.keys() :
			field = parm['field']
		else:
			field = '*'
		# SQL语句
		sql = 'SELECT '+field+' FROM `'+table+'`'
		if 'where' in parm.keys() :
			sql += ' WHERE '+parm['where']
		if 'order' in parm.keys() :
			sql += ' ORDER BY '+parm['order']
		if 'limit' in parm.keys() :
			sql += ' LIMIT '+parm['limit']

		print(sql)

		sql = 'select * from cqssc'
		# 游标
		cursor=self.__cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	# 查询一条
	def findfirst(self,parm=''):
		sql = 'select * from cqssc'
		# 游标
		cursor=self.__cursor()
		cursor.execute(sql)
		return cursor.fetchone()

	# 返回条数
	def getRows(self):
		sql = 'select * from cqssc'
		# 游标
		cursor=self.__cursor()
		cursor.execute(sql)
		cursor.fetchall()
		return cursor.rowcount

	# 添加
	def add(self,table='',data=''):
		if table=='' or data=='' :
			print({'state':'n','msg':'请传入参数！'}); exit()
		# 数据
		k = '`,`'.join(data)
		v = '\',\''.join(data.values())
		# SQL语句
		self.__sql += ['INSERT INTO '+table+' (`'+k+'`) VALUES (\''+v+'\')']
		return self

	# 更新
	def update(self,table='',data='',where=''):
		if table=='' or data==''  or where=='' :
			print({'state':'n','msg':'请传入参数！'}); exit()
		# 数据
		v = ''
		for (key,val) in data.items():
			v += '`'+key+'`=\''+val+'\','
		v = v.rstrip(',')
		# SQL语句
		self.__sql += ['UPDATE '+table+' SET '+v+' WHERE '+where]
		return self

	# 删除
	def delete(self,table='',where=''):
		if table=='' or where=='' :
			print({'state':'n','msg':'请传入参数！'}); exit()
		# SQL语句
		self.__sql += ['DELETE FROM '+table+' WHERE '+where]
		return self

	# 执行SQL
	def commit(self):
		# 游标
		cursor=self.__cursor()

		try:
			# 执行SQL
			for val in self.__sql :
				cursor.execute(val)
			# 提交
			self.cnn.commit()
			return True
		except mysql.connector.Error as e:
			# 回滚
			self.cnn.rollback()
			return {'state':'n','msg':'执行SQL错误！{}'.format(e)}
		finally:
			self.cnn.close()

		# 获取游标
	def __cursor(self):
		# 链接数据库
		try:
			self.cnn=mysql.connector.connect(**self.config)
			# 返回游标
			return self.cnn.cursor(dictionary=True)
		except mysql.connector.Error as e:
			print({'state':'n','msg':'链接数据库错误！{}'.format(e)}); exit()
