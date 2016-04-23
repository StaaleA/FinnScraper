from lxml import html
from datetime import datetime
import requests
import boto3
import sys

# Gets info about two search terms; "datavarehus" and "business intelligence"
datavarehus = requests.get('http://m.finn.no/job/fulltime/search.html?q=datavarehus&industry=65&industry=8&industry=34&sort=1')
businessIntelligence = requests.get('http://m.finn.no/job/fulltime/search.html?q=business+intelligence&industry=65&industry=8&industry=34&sort=1')

# Extracts the number of jobs and ads
tree = html.fromstring(datavarehus.content)
datavarehus_count = tree.xpath('//span[@class="current-hit-count"]/b[@data-count]/text()') #['Stillinger', 'Annonser']

tree = html.fromstring(businessIntelligence.content)
businessIntelligence_count = tree.xpath('//span[@class="current-hit-count"]/b[@data-count]/text()') #['Stillinger', 'Annonser']

# Sets the date
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Builds the output text
datavarehus_stillinger = datavarehus_count[0];
datavarehus_annonser = datavarehus_count[1];
datavarehusTekst = "datavarehus,"+datavarehus_stillinger+","+datavarehus_annonser+","+date

businessIntelligence_stillinger = businessIntelligence_count[0];
businessIntelligence_annonser = businessIntelligence_count[1];
businessIntelligenceTekst = "business intelligence,"+businessIntelligence_stillinger+","+businessIntelligence_annonser+","+date

# Gets the file location as an argument
if len(sys.argv) != 2:
    sys.exit('Usage: .../webScraper.py fileLocation') # If a file location hasent been passed as an argument
else:
	fileLocation = sys.argv[1]

# Appends the file with the new data
try:
	file = open(fileLocation,"a")
except IOError:
        print('Cannot open file. Check the that you have the correct file location', arg)
else:
	file.write(datavarehusTekst +"\r\n")
	file.write(businessIntelligenceTekst+"\r\n")
	file.close()

# Upload the file to S3
s3_client = boto3.client('s3')
s3_client.upload_file(fileLocation, 'samedia', 'stillinger.csv')