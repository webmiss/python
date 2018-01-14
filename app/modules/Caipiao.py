#!/bin/python
# -*- coding: UTF-8 -*-

from urllib import request
import gzip
import re
import time
import json

from framework.MySQL import MySQL
# from framework.Email import Email

# 
# 彩票
# 
class Caipiao:
	# 首页
	def index(self) :
		print('彩票首页')

	# 重庆时时彩
	def cqssc(self):
		# 期数
		periodF = 'upload/period.txt'
		period = self.__getPeriod(periodF)
		# Html
		date = time.strftime("%Y%m%d", time.localtime())
		url = 'http://caipiao.163.com/award/daily_refresh.html?cache=1514042208192&gameEn=ssc&selectDate=1&date='+date
		html = self.__getHtml(url)
		# 彩票号码
		num = self.__getNum(html,period)
		if period=='120' :
			# Html
			url = 'http://f.apiplus.net/cqssc-1.json'
			html = request.urlopen(url).read()
			html = html.decode('utf-8')
			# Num
			s = json.loads(html);
			date = str(int(date)-1)
			if (date+period)==s['data'][0]['expect'] :
				num = s['data'][0]['opencode'].split(',')

		#  数据
		if num :
			res = True
			# 是否存在
			isNull = MySQL().findfirst({'table':'cqssc','where':'date="'+date+'" and period='+period})
			if isNull==None :
				# 记录数据
				res = MySQL().add(
					'cqssc',
					{'date':date,'period':period,'num1':num[0],'num2':num[1],'num3':num[2],'num4':num[3],'num5':num[4]}
				).commit()
			#  写入期数
			if res == True :
				f = open(periodF,'w')
				f.write(str(int(period)+1).zfill(3))
				f.close()
			else:
				print(res)
		# 提示
		print(date,period,num)

	# 读取期数
	def __getPeriod(self,file):
		f = open(file)
		period = f.read().strip()
		f.close()
		# 最大期数
		if period=='121' or period=='' :
			period = '001'
		return period;

	# 获取html
	def __getHtml(self,url):
		html = request.urlopen(url).read()
		# 解码
		try:
			html = gzip.decompress(html).decode('utf-8')
		except:
			html = html.decode('utf-8')
		return html

	# 开奖号码
	def __getNum(self,html,period):
		reg = r'<td class="start" data-win-number=\'(.+)\' data-period="(.+)">'+period+'</td>'
		num = re.findall(reg,html)
		if num :
			num = re.findall(r'([0-9])',num[0][0])
		return num
