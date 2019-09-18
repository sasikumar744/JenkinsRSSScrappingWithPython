import urllib,urllib2,base64,datetime,re,sys
from bs4 import BeautifulSoup
from datetime import date,timedelta

#ydate = str(datetime.date.today()-timedelta(1))
ydate = str(datetime.date.today())
#print ydate

#This method formats credentials
def auth_headers(username, password):
   return 'Basic ' + base64.encodestring('%s:%s' % (username, password))[:-1]

#Credentials go here
auth = auth_headers(sys.argv[1], sys.argv[2])
#Home page url
homeUrl = sys.argv[3]
#RSS url
rssUrl = homeUrl+'/rssAll'
#This completes authentication and reads data from RSS url
req = urllib2.Request(rssUrl)
req.add_header('Authorization', auth)

#List and variables declaration
prodJobsTitles,prodJobsTitlesTriggerTime = [],[]
i,j = 0,0

#Fetching RSS feed
rssFeed = urllib2.urlopen(req).read()

#Formatting RSS feed to xml format
rssFeedXml = BeautifulSoup(rssFeed,"lxml")

#Extracting all entries from xml
entries =  rssFeedXml.find_all('entry')
entriesString = str(entries)
#print entriesString.count(str(ydate))
count = entriesString.count(str(ydate))/2

#Enter loop only if entries found for ydate
if count != 0 :
	#Iterating over all entries
	print 'No.of jobs ran on '+str(ydate)+': '+str(count)
	print 'Below jobs ran on '+str(ydate)
	for e in entries:
		#if ydate in e.find('published'):
		if re.search(str(ydate),str(e)):
			Title,TriggerTime = e.find('title'),e.find('published')
			TitleTrim = re.findall(re.escape('<title>')+"(.*)"+re.escape('</title>'),str(Title))[0]
			TriggerTimeTrim = re.findall(re.escape('<published>')+"(.*)"+re.escape('</published>'),str(TriggerTime))[0]
			if ('prod' in TitleTrim or 'master' in TitleTrim) :
				#print 'This is prod job'
				#print TitleTrim,'\t',TriggerTimeTrim
				#prodjobs = prodJobs.append(TitleTrim).append(str(',\t,')).append(TriggerTimeTrim).append(str(',\n'))
				prodJobsTitles.insert(i,TitleTrim)
				prodJobsTitlesTriggerTime.insert(i,TriggerTimeTrim)
				i = i+1
				#print '\n'
			else :
				print TitleTrim,'\t',TriggerTimeTrim
	#print prodJobsTitles,prodJobsTitlesTriggerTime
	if (i>0) :
		print '\n\nBelow are the prod jobs that ran on '+str(ydate)
		while (j<i) :
			print prodJobsTitles[j],'\t',prodJobsTitlesTriggerTime[j]
			j = j+1	
else:
	print 'No jobs ran on '+str(ydate)	
