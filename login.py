import requests
from urllib.request import urlopen
import webbrowser
from bs4 import *


def Login(username,password):

	with requests.session() as s:
		url="http://www.scholfin.com/login/"
		dash_url="http://www.scholfin.com/dashboard/"
		s.get(url)
		csrftoken=s.cookies['csrftoken']
		login_data=dict(csrfmiddlewaretoken=csrftoken,username=username,password=password)
		s.post(url,data=login_data)
		page=s.get("http://www.scholfin.com/dashboard/",headers=dict(referer="http://www.scholfin.com/dashboard/"))
		soup=BeautifulSoup(page.content,'lxml')
		f=open("D:/AAHAN/aahan/django/api/apiapp/apisearch/templates/dashboard.html","w")
		#amount_tags=soup.find_all("span",{})
		head_tags=soup.find_all("div",{"class":"table-column name mdl-cell--2-col"})
		f.write("Hello Aahan, Your scholarship dashboard")
		'''for atags in amount_tags:
			f.write(str(atags)+"\n")'''
		for htags in head_tags:
			f.write(str(htags)+"\n")
		f.close()

		fileurl="D:/AAHAN/aahan/django/api/apiapp/apisearch/templates/dashboard.html"
		webbrowser.open(fileurl)
		


def main():
	username=input("Username: ")
	password=input("Password: ")
	Login(username,password)

if __name__ == '__main__':
	main()
