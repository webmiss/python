#!/bin/python
# -*- coding: UTF-8 -*-

import sys

# 获取参数
parameter = sys.argv
# 默认参数
from app.config import *
param = [config['modules'],config['action'],'','']

# 模块、函数、参数
if len(parameter)==2 :
	param[0] = parameter[1]
if len(parameter)==3 :
	param[1] = parameter[2]
if len(parameter)==4:
	param[2] = parameter[3]
if len(parameter)==5:
	param[3] = parameter[4]

# 加载模块
exec('from app.modules.'+param[0]+' import *')
# 实例化
exec('c = '+param[0]+'('+param[3]+')');
# 动作函数
exec('c.'+param[1]+'('+param[2]+')');
