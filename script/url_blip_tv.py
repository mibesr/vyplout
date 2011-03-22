import re
import urllib

#config
rss_url="http://pycon.blip.tv/rss"   #rss feed list
html_file="pycon2011.html"           #html file name

#parse
f = urllib.urlopen(rss_url)
content=f.read()

regex=r'http://blip.tv/file/get/Pycon\-PyCon2011(?P<name>.*?)\.mp4'   #regex PyCon2011's mp4


reobj=re.compile(regex)

html="<html><head><title>pycon2011</title></head><body>"


url_list=[]
for abc in reobj.finditer(content):
	print abc.group()
	url=abc.group()
	if(url not in url_list):
		url_list.append(url)
		html=html+"<a href='{0}'>{0}</a><br>\n".format(url)


#write
html=html+"</body></html>"

html_file = open(html_file, 'w')
html_file.write(html);

