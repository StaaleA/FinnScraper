# FinnScraper
A simple web scraper that gets the number of classified ads with a specific search term on finn.no. The result is saved in a .csv-file and uploaded to a S3 bucket. 
The script is running daily on a EC2 instance with help of crontab.

## Dependencies
lxml
```
sudo yum install python-devel
sudo yum install libxml2-devel
sudo yum install libxslt-devel  
sudo yum install gcc        
sudo easy_install pip
sudo pip install lxml
```

Boto3
```
sudo pip install boto3
```