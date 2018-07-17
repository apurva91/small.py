import requests, os
from getpass import getpass

baseurl="https://intranet.iitg.ernet.in/moodle"
loginurl="https://intranet.iitg.ernet.in/moodle/login/index.php"

def GetFileName(res):
	return str(res.headers).split('filename="')[1].split('"')[0]

def SaveFile(basename,res):
	filename = GetFileName(res)
	open(basename+'/'+filename,'wb').write(res.content)
	print (basename+'/'+filename + " saved successfully.\n")

def CrawlGet(start,end,code):
	urls=[]
	for item in code.split(end):
		if start in item:
			urls.append(item [item.find(start)+len(start) : ])

	return urls

def FolderSave(name,url):
	res = client.get(url)
	urls2=CrawlGet('<span class="fp-filename-icon"><a href="','?forcedownload=1">',str(res.content))
	name2 = name+'/'+ CrawlGet('<h2>','</h2>',str(res.content))[0]
	if not os.path.isdir(name2):
		os.mkdir(name2)
	for item in urls2:
		SaveFile(name2,client.get(item))

def CourseSave(url,name):

	res = client.get(url)
	print ("Do You want to save the course " + name+'(y/n)')
	user_resp = input()
	if user_resp =='n':
		return
	if not os.path.isdir(name):
		os.mkdir(name)
	
	urls = CrawlGet('<div class="activityinstance"><a class="" onclick="" href="','"><img src="',str(res.content))

	for item in urls:
		if item.find("resource") is not -1:
			SaveFile(name,client.get(item))
		if item.find("folder") is not -1:
			FolderSave(name,item)
		if item.find("page") is not -1:
			print ("Visit " + item + " it is static page.\n")
		if item.find("url") is not -1:
			print ("Visit " + item + " it is static page.\n")

	print (name + " : Course Saved Successfully")

client = requests.session()
print ("Enter Your Username:")
username=input()
print ("Enter Your Password:")
password=getpass()
rememberusername='1'
data = dict(username=username,password=password,rememberusername=rememberusername)
r = client.post(loginurl,data=data)
if r.status_code is 200:
	print ("Logged in Successfully.\nStarting Downloading.")
	res = client.get(baseurl)
	urlinfo = CrawlGet('<div class="panel-heading info"><span class="coursename">','</span><span class="moreinfo"></span></div>',str(res.content))
	for urlin in urlinfo:
		CourseSave(urlin.split('"')[3],CrawlGet('>','</',urlin.split('"')[4])[0])
else:
	print ("Unable to Login.")