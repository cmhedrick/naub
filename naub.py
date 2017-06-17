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
# you need the end encoding after the message
END = '\033[0m'
# DEBUG INFO
DEBUG = True

# set basic globals
cmd_base_url = ''
cmd = ''
robot_urls = []
# maybe an ignore list for bad names
ignore_list = [
    '*'
]

print('\n------------------------------')
print('            naub              ')
print('The handle to a new adventure!')
print('------------------------------')

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

def test_urls(url_wordlist=None, base_url=None):
    for url in robot_urls:
        try:
            response = urllib.request.urlopen(base_url + url)
            if response.code == 200:
                if DEBUG:
                    print(SUCCESS + '[+]' + END + url)

        except urllib.error.HTTPError as e:
            if DEBUG:
                print('{0}{1}'.format(ALERT + '[!]' + END, e.code))

        except urllib.error.URLError as e:
            if DEBUG:
                print('{0}{1}'.format(ALERT + '[!]' + END, e.code))

if __name__ == "__main__":
    while cmd != 'q'.lower():
        # display menu and get cmd
        print('\nenter a command:')
        print('set | set url of site and bruteforce')
        print('q | kill session')
        cmd = input('==> ')

        if cmd == 'set'.lower():
            robot_urls = []
            try:
                if config.URL and config.URL.strip() != '':
                    cmd_base_url = config.URL
                else:
                    cmd_base_url = input('URL==> ')
            except:
                cmd_base_url = input('URL==> ')

            print(SUCCESS + '[+]' + END + 'URL set')
            print(NOTICE + '[#]' + END + 'checking robots.txt')
            get_robot_urls(cmd_base_url)
            test_urls(base_url=cmd_base_url)

        elif cmd == 'q'.lower():
            print(NOTICE + '[XXX]' + END + ',.-\'*^GAME_OVER^*\'-.,')

        else:
            print(ALERT + '[!]' + END + 'INVALID COMMAND')
