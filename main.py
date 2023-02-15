import requests
from bs4 import BeautifulSoup

from payloads import payloads as xss_payloads


class XssChecker:
    def get_html(url):
        response = requests.get(url)
        return response.text

    def ScanningForxss(html):
        soup = BeautifulSoup(html, 'html.parser')
        for payload in xss_payloads:
            if payload in str(soup):
                response = f"[XSS VULNERABILITY FOUND] Payload: {payload}"
                return response
