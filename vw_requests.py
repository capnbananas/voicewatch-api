from Epoch_range_finder import *
import requests
import re

url_dict = {}
test_dict = {}

def all_tests():
  with requests.Session() as s:
    # auth
    vw_login_json = 'https://services-sso.empirix.com/openam/json/authenticate'
    s.headers.update({"Host": "services-sso.empirix.com", 'Content-API-Version': 'protocol=1.0,resource=2.0', 'Content-Type': 'application/json;charset=UTF-8'})
    vw_header = s.post(vw_login_json).headers
    vw_jsdict = s.post(vw_login_json).json()
    vw_jsdict['callbacks'][0]['input'][0].update({'value': "user"})
    vw_jsdict['callbacks'][1]['input'][0].update({'value': "pass"})
    vw_login = s.post(vw_login_json, json=vw_jsdict).json()
    vw_token = 'iPlanetDirectoryPro=' + vw_login['tokenId']
    vw_cookie = re.split(';', vw_header['Set-Cookie'])[0] + ";" + ' ' + vw_token
    s.headers.update({"Cookie": vw_cookie})
    # testing_dict = s.get('https://services.empirix.com/webapp//vw-dashboard').json()
    # list_of_tests = testing_dict['tests_info']
    list_of_tests = [4541]
    for test in list_of_tests:
      test_urls(test)
    for url in epoch_test_urls:
      url_js = s.get(url).json()
      vw_pass = 0
      vw_fail = 0
      vw_alert = 0
      try:
        Test_data = url_js["test_results"][0]
        test_name = Test_data["test_name"]
        instance_list = Test_data['test_instances']
        # print(instance_list)
        for instance in instance_list:
          if instance['error_step_detail'] is None:
            vw_pass += 1
            url_dict.update({test_name: [vw_pass, vw_fail, vw_alert]})
          else:
            vw_fail += 1
            url_dict.update({test_name: [vw_pass, vw_fail, vw_alert]})
        for alert in instance_list:
          if alert['total_alerts'] == 1:
            vw_alert += 1
            url_dict.update({test_name: [vw_pass, vw_fail, vw_alert]})
      except:
        pass






