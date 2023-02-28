import requests
from bs4 import BeautifulSoup

from payloads import payloads as xss_payloads
import re


class XssChecker:

    def get_html(url):
        response = requests.get(url)
        return response.text

    def ScanningForxss(html):
        ListVulnerability = []
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all(True):
            if tag.name not in ['a', 'img', 'br']:
                for attr, value in tag.attrs.items():
                    pattern = re.compile(r"<.*script.*>")
                    if pattern.search(value):
                        response = f"[XSS VULNERABILITY FOUND] Tag: {tag.name}, Attribute: {attr}, Value: {value}"
                        ListVulnerability.append(response)
        return ListVulnerability

        # print(ListVulnerability)
        # return ListVulnerability
