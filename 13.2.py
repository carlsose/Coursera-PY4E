#Extracting Data from JSON

#http://py4e-data.dr-chuck.net/comments_116455.json

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_116455.json (Sum ends with 70)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 

import urllib.request
import json

url = input('Enter location: ')
print('Retrieving', url)
input = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(input), 'characters')
info = json.loads(input)

count = 0
sum = 0
for i in range(0, len(info['comments'])):
    count = count + 1
    sum = sum + int(info['comments'][i]['count'])

print('Count:', count)
print('Sum:', sum)
