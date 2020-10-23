#Import the REQUESTS package
import requests

# Define a URL to request
url = "http://www.npr.org"

# Write the response
response = requests.get(url)

print(f"your request to {url} came back with the status code {response.status_code}")

print(response.text)