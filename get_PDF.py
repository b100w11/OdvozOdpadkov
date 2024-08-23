#!/usr/bin/env python3
# Import libraries
import requests
from bs4 import BeautifulSoup
# Year to download
year = "2024"

# id
id = "urnik-" + year
# save path
save="data/" + year + "/pdf"

# URL from which pdfs to be downloaded
url = "https://www.komunala-sezana.si/dejavnosti/ravnanje-z-odpadki/urniki-odvoza-odpadkov"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')
i = 0

# From all links check for pdf link and
# if present download file
for link in links:
	###print(link)
	if (id in link.get('href', [])):
		if ('.pdf' in link.get('href', [])):
			i += 1
			print("Downloading file: ", i)

			# Get response object for link
			response = requests.get(link.get('href'))

			# Write content in pdf file
			pdf = open(save + "/"+str(i) + ".pdf", 'wb')
			pdf.write(response.content)
			pdf.close()
			print("File ", i, " downloaded")

print("All PDF files downloaded to " + save)

