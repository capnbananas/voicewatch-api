import requests
import re


def disable_test(test_nums):
  with requests.Session() as s:
    # auth
    vw_login_json = 'https://services-sso.empirix.com/openam/json/authenticate'
    s.headers.update({"Host": "services-sso.empirix.com", 'Content-API-Version': 'protocol=1.0,resource=2.0', 'Content-Type': 'application/json;charset=UTF-8'})
    vw_header = s.post(vw_login_json).headers
    vw_jsdict = s.post(vw_login_json).json()
    vw_jsdict['callbacks'][0]['input'][0].update({'value': "username"})
    vw_jsdict['callbacks'][1]['input'][0].update({'value': "pass"})
    vw_login = s.post(vw_login_json, json=vw_jsdict).json()
    vw_token = 'iPlanetDirectoryPro=' + vw_login['tokenId']
    vw_cookie = re.split(';', vw_header['Set-Cookie'])[0] + ";" + ' ' + vw_token
    s.headers.update({"Cookie": vw_cookie})
    test_url = 'https://services.empirix.com/webapp/tests/'
    test_json = s.get(test_url + str(test_nums)).json()
    print(test_json)
    print('\n')
    test_json.update({'disabled': 1})
    s.post('https://services.empirix.com/webapp/tests', json=test_json)
    test_json2 = s.get(test_url + str(test_nums)).json()
    print(test_json2)





# testing with 6434
# you can pass a list for multiple tests

disable_test(6434)