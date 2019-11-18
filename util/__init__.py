#coding:utf-8

"""
    author : linkin
    date   : 2019-11-18
    QQ     : 1057211448
"""

import re

def from_pattern(pattern,text,index:int=0,ALL:bool=False):
	res = re.findall(pattern,text)
	if res:
		if not ALL:
			data = res[index]
			return data
		else:
			return res