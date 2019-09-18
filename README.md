# JenkinsRSSScrappingWithPython
This script can be used to scrape Jenkins RSS feed.
2. Upon successful run this job displays the name and trigger time of Jenkins jobs that ran on previous day.
3. This job uses BeautifulSoup hence bs4 pip installation is mandatory.
4. As part of reading data, we convert data into xml format. Hence lxml package installation required.
5. Below is the format to execute this job
   python JeniinsRSSScrappingWithPython.py 'JenkinsUser' 'JenkinsUserPassword' 'http://JenkinsHost:JenkinsPort'
