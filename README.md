# naub
naub (not-another-URL-Brute-Forcer): Pronounced like "knob" in "doorknob" is INDEED another URL brute-forcer. Module can be ran as a standalone or can be imported into another module.
##### Disclaimer:
_Please be careful while using this script. To many requests under a short amount of time could appear as a possible DoS (Denial of Service) attack. Use with caution and responsibly._

## Installation:
1. First clone the repo
`git clone https://github.com/cmhedrick/naub.git`
2. Change into the naub directory
`cd naub`
3. Create copy of the url `config.py.copy` file and call it `config.py`
`cp config.py.copy config.py`
4. Open the `config.py` file and edit the settings.
    1. `URL` is a string object, for the URL you want to target.
    2. `URL_WORDLIST` is a string object, meant to be the path to your wordlist.
    3. `DEBUG` is a bool object, helps enables verbosity of functions. Reccomended use with the file running as main.
    4. `WRITE_TO_FILE` bool object, that has `test_urls()` write to external file.

## Functions:
`get_robot_urls(url)`:
Param `url`: is a string meant to be the url e.g: http://example.com/
Purpose: Creates and returns a python list object based on URLs found in the supplied URL's Robots.txt file if applicable.

`parse_url_list(path)`:
Param `path`: is a string, meant to be a path to a wordlist text file. *See included url_list.txt for example of file format.*
Purpose: Creates and returns a python list object based on URL extensions found in the wordlist file.

`test_urls(url_wordlist, base_url)`:
Param `url_wordlist`: is python list object of url extentions.
Param `base_url`: is a string meant to be a url.
Purpose: uses given wordlist to ping various extension urls to check if they exist. Will return list of existing urls. Will also write discovered URL exstensions that returned positive HTTP responses to a txt file if `WRITE_TO_FILE` is `True`.