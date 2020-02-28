#python2.7
import os,sys,re,time
import urllib2
import requests
import httplib
import ssl
import multiprocessing
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass
print("_  __________ ____   _____  __________  _________ ")
print("|__| |  | |__][__    |   |__||___|   |_/ |___|__/ ")
print("|  | |  | |   ___]   |___|  ||___|___| \_|___|  \ ")
print(green+"Author By"+red+" Sterben404"+reset)
def error():
	try:
		open(sys.argv[1], 'rb')
	except IOError:
		print(red+"[ - ]"+reset+" File Not Found!")
		exit()
	except IndexError:
		print(red+"[ - ]"+reset+" Usage : python2 file.py list.txt")
		exit()

error()

def proc(url):
	try:
		url = url.replace('http://','').replace('https://','')
		req = urllib2.Request('https://'+url, headers={'User-Agent': 'Mozilla/5.0'})
		sites = urllib2.urlopen(req, timeout=7)

	except (urllib2.URLError,ssl.CertificateError,ssl.SSLError):
		print('https://'+url+red+" --> HTTP"+reset)
		with open('webhttp.txt','ab') as http:
			http.write('http://'+url+'\n')
			http.close()
	else:
		print('https://'+url+green+" --> HTTPS"+reset)
		with open('webhttps.txt','ab') as https:
			https.write('https://'+url+'\n')
			https.close()
	pass
lists = open(sys.argv[1], 'rb').read().splitlines()
t = ThreadPool(15)
t.map(proc, lists)
t.close()
t.join()

if __name__ == "__main__":
	print(green+"Save File HTTPS: webhttps.txt")
	print(red+"Save File HTTP: webhttp.txt")
	print(blue+"Tools by Sterben404"+reset)
