# FinnScraper
A simple web scraper that gets the number of classified ads with a specific search term on finn.no. The result is saved in a .csv-file and uploaded to a S3 bucket. Currently this is running locally using launchd in OSX.

## Dependencies
```
sudo yum install python-devel
sudo yum install libxml2-devel
sudo yum install libxslt-devel  
sudo yum install gcc        
sudo easy_install pip
sudo pip install lxml
```