#!/usr/bin/python3
import urllib.parse
import urllib.request

# love the config files
import config

# colors
# blue special notice
NOTICE = '\033[94m'
# red is important
ALERT = '\033[91m'
# green is Good
SUCCESS = '\033[92m'
# yellow when not quite right
WARN = '\033[93m'
# you need the end encoding after the message
END = '\033[0m'
# DEBUG INFO
DEBUG = True

# set basic globals
cmd_base_url = ''
url_list = []
cmd = ''
robot_urls = []
# maybe an ignore list for bad names
ignore_list = [
    '*'
]
# acceptable responses
accept_list = [
    403
]

def get_robot_urls(url):
    '''
    gets urls in robots.txt file
    :param url: string
    :return: list
    '''
    try:
        response = urllib.request.urlopen(url + 'robots.txt')
        if response.code == 200:
            for line in response:
                conv_line = line.split()[1].decode("utf-8")
                if conv_line in ignore_list:
                    pass
                else:
                    # remove the disallow or allow or possible other predicate
                    robot_urls.append(conv_line)
            if DEBUG:
                print(NOTICE + '[#]' + END + 'URL List: ' + str(robot_urls))
            return robot_urls

    except urllib.error.HTTPError as e:
        if DEBUG:
            print('{0}{1}'.format(ALERT + '[!]' + END, e.code))
        return robot_urls

    except urllib.error.URLError as e:
        if DEBUG:
            print('{0}{1}'.format(ALERT + '[!]' + END, e.code))
        return robot_urls

def parse_url_list(path):
    global  url_list
    url_list = []
    with open(path) as url_txt:
        for line in url_txt:
            conv_line = line.strip()
            if DEBUG:
                print(SUCCESS + '[+]' + END + 'Added: ' + conv_line)
            url_list.append(conv_line)

    return url_list

def test_urls(url_wordlist=None, base_url=None):
    if url_wordlist:
        results = open('results.txt', 'w')
        for url in url_wordlist:
            try:
                response = urllib.request.urlopen(base_url + url)
                if response.code == 200:
                    if DEBUG:
                        print(SUCCESS + '[+]' + END + url)
                    results.write(
                        '[{0}]: {1}'.format(
                            response.code,
                            url
                        )
                    )

            except urllib.error.HTTPError as e:
                if DEBUG:
                    if e.code in accept_list:
                        print('{0}{1}'.format(WARN + '[^]' + END, e.code))

                    else:
                        print('{0}{1}'.format(ALERT + '[!]' + END, e.code))

                if e.code in accept_list:
                    results.write(
                        '[{0}]: {1}\n'.format(
                            e.code,
                            url
                        )
                    )

            except urllib.error.URLError as e:
                if DEBUG:
                    if e.code in accept_list:
                        print('{0}{1}'.format(WARN + '[^]' + END, e.code))
                    else:
                        print('{0}{1}'.format(ALERT + '[!]' + END, e.code))

                if e.code in accept_list:
                    results.write(
                        '[{0}]: {1}'.format(
                            e.code,
                            url
                        )
                    )

        results.close()

if __name__ == "__main__":
    print('\n------------------------------')
    print('            naub              ')
    print('The handle to a new adventure!')
    print('------------------------------')

    while cmd != 'q'.lower():
        # display menu and get cmd
        print('\nenter a command:')
        print('set | set vars for bruteforce')
        print('q | kill session')
        cmd = input('==> ')

        if cmd == 'set'.lower():
            robot_urls = []
            try:
                if config.URL and config.URL.strip() != '':
                    cmd_base_url = config.URL
                else:
                    cmd_base_url = input('URL==> ')
                if config.URL_WORDLIST and config.URL_WORDLIST.strip() != '':
                    url_wordlist = config.URL_WORDLIST
                else:
                    url_wordlist = input('PATH TO URL_LIST==> ')

            except:
                cmd_base_url = input('URL==> ')
                url_wordlist = input('PATH TO URL_LIST==> ')

            print(SUCCESS + '[+]' + END + 'URL set')
            print(SUCCESS + '[+]' + END + 'URL_LIST set')
            print(NOTICE + '[#]' + END + 'checking robots.txt')
            get_robot_urls(cmd_base_url)
            print(NOTICE + '[#]' + END + 'converting url wordlist')
            parse_url_list(url_wordlist)
            # extend url_list by robot urls
            url_list.extend(robot_urls)
            print(NOTICE + '[#]' + END + 'starting bruteforce')
            test_urls(url_wordlist=url_list,base_url=cmd_base_url)

        elif cmd == 'q'.lower():
            print(NOTICE + '[XXX]' + END + ',.-\'*^GAME_OVER^*\'-.,')

        else:
            print(ALERT + '[!]' + END + 'INVALID COMMAND')
