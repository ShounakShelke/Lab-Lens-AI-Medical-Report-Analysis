import requests
try:
    r = requests.get('http://localhost:5000/api/demo/high-risk')
    print(r.status_code)
    print(r.json()['data']['riskSummary']['bannerMessage'])
except Exception as e:
    print(e)
