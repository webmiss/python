# 
# Email类
# ----------------------------------------------

import smtplib
from email.mime.text import MIMEText
# 配置文件
from app.smtp import smtp

class Email:

	# 构造函数
	def __init__(self):
		self.smtp = smtp

	# 发送邮件
	# parm: {'to':['收件人'], 'subject':'标题', 'content':'内容'}
	def sendSmtp(self,parm=''):
		me = self.smtp['alias']+"<"+self.smtp['user']+"@"+self.smtp['postfix']+">"
		to_list=parm['to']
		# MSG
		msg = MIMEText(parm['content'],_subtype='plain')
		msg['Subject'] = parm['subject']
		msg['From: '] = me
		msg['To'] = ";".join(to_list)
		# 发送邮件
		try:
			server = smtplib.SMTP()
			server.connect(self.smtp['host'],self.smtp['port'])
			server.login(self.smtp['user'],self.smtp['passwd'])
			server.sendmail(me, to_list, msg.as_string())
			server.close()
			return True
		except Exception as e:
			return {'state':'n','msg':'发送失败：{}'.format(e)}