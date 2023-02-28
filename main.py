import requests
from payloads import payloads as xss_payloads


class XssChecker:
    def get_html(url):
        return url

    def ScanningForxss(targetWebsite):
        ResponseList = []
        for payload in xss_payloads:
            responseDict = {}
            response = requests.post(targetWebsite+payload)
            if payload in response.text:
                responseDict["payload"] = payload
            else:
                print("no payload found")
            ResponseList.append(responseDict)

        return ResponseList
