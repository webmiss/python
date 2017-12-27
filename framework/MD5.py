# 
# MD5类
# ----------------------------------------------

import hashlib

class MD5:
	def get(self,str=''):
		m = hashlib.md5()
		m.update(str.encode('UTF-8'))
		return m.hexdigest()