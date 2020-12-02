from vw_requests import *
from Epoch_range_finder import *

date_range([[2020, 5, 18], [2020, 5, 25]])
pl = []
fl = []
al = []
od = {}

# testing_dict = s.get('https://services.empirix.com/webapp//vw-dashboard').json()
# All tests is here to scaleable
# list_of_tests = testing_dict['tests_info']
# list_of_tests = [1461, 1564, 2777, 2944, 2884]

all_tests()
# 
print(epoch_test_urls)
# 
# get_test_keys2(url_dict)
# 
# for test in test_keys2:
  # pl.append(url_dict[test][0])
  # fl.append(url_dict[test][1])
  # al.append(url_dict[test][2])
# 
# pt = sum(pl)
# ft = sum(fl)
# at = sum(al)
# 
# print("Wells Fargo")
# print("Total Passing Tests: " + str(pt))
# print("Total Failing Tests: " + str(ft))
# print("Total Alerts: " + str(at) + '\n')
# 
# for test in test_keys2:
  # print('Test Name: ' + test)
  # print("Total Passing: " + str(url_dict[test][0]))
  # print("Total Failing: " + str(url_dict[test][1]))
  # print("Total Alerts: " + str(url_dict[test][2]) + '\n')

# print(url_dict)