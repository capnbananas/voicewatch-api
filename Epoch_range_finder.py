from datetime import date, timedelta
import time

# input 2 dates in a list format [[year, month, day], [year, month, day]] to find a range of Epoch dates then creates a list of testless urls.
test_keys = []
test_keys2 = []

def get_test_keys(dict): 
  for key in dict.keys(): 
    test_keys.append(key)

def get_test_keys2(dict): 
  for key in dict.keys(): 
    test_keys2.append(key)

epoch_vw_str = []

def date_range(dates_in_list):
  start_date = date(dates_in_list[0][0], dates_in_list[0][1], dates_in_list[0][2])
  end_date =  date(dates_in_list[1][0], dates_in_list[1][1], dates_in_list[1][2])
  delta = end_date - start_date 
  for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    t_s = str(day.day) + ' ' + str(day.month) + ',' + ' ' + str(day.year)
    a = time.strptime(t_s, "%d %m, %Y")
    b = time.mktime(a)
    epoch_vw_str.append("https://services.empirix.com/webapp/test-results?noCache=&retrieval_timestamp=" + str(int(b)) + "&test_ids=")

epoch_test_urls = []

def test_urls(vw_test):
  for i in epoch_vw_str:
    epoch_test_urls.append(i + str(vw_test))