import requests
from bs4 import BeautifulSoup
import re

# Define a function to detect XSS vulnerabilities in the HTML


def detect_xss_vulnerabilities(html):
    xss_payloads = [
        '<script>alert("XSS");</script>', '<img src="x" onerror="alert(\'XSS\');">']
    vulnerabilities = []
    for key, value in html.items():
        for payload in xss_payloads:
            pattern = re.compile(re.escape(payload), re.IGNORECASE)
            if pattern.search(value):
                vulnerabilities.append(
                    f'XSS vulnerability detected in {key} parameter with payload "{payload}"')
    return vulnerabilities


# Set up a session with DVWA
session = requests.session()
session.get('http://localhost/dvwa/login.php')
data = {'username': 'admin', 'password': 'password', 'Login': 'Login'}
session.post('http://localhost/dvwa/login.php', data=data)

# Retrieve the HTML of the XSS page
url = 'http://localhost/dvwa/vulnerabilities/xss_r/'
response = session.get(url)
html = BeautifulSoup(response.content, 'html.parser')

# Detect XSS vulnerabilities in the HTML
vulnerabilities = detect_xss_vulnerabilities(html)
if vulnerabilities:
    print("The following XSS vulnerabilities were detected:")
    for vulnerability in vulnerabilities:
        print(vulnerability)
else:
    print("No XSS vulnerabilities detected.")
