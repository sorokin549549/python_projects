import csv
import io
import urllib.request


url = 'https://docs.google.com/spreadsheets/d/1NMCnmWy7hn-gNO7oyQyaM_WBmUR3kO9xzjQQ1iopbhk/export?format=csv'

response = urllib.request.urlopen(url)

with io.TextIOWrapper(response, encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0].lower().replace(' ', '.'))
