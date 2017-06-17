import naub
import config

url_list = []
# get robot urls
robot_urls = naub.get_robot_urls(config.URL)
# parse url wordlist file
url_list.extend(naub.parse_url_list(config.URL_WORDLIST))
# add robot urls to list
url_list.extend(robot_urls)
# begin test and create the results
print(naub.test_urls(url_wordlist=url_list,base_url=config.URL))
