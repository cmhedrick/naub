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
base_url = ''
cmd = ''
robot_urls = []
# maybe an ignore list for bad names
# ignore_list = [
#     b'User-agent: *'
# ]

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
                if line.startswith(b'User-agent: *'):
                    pass
                else:
                    # remove the disallow or allow or possible other predicate
                    robot_urls.append(line.split()[1].decode("utf-8"))
            if DEBUG:
                print(NOTICE + '[#]' + END + str(robot_urls))
            return robot_urls

    except urllib.error.HTTPError as e:
        if DEBUG:
            print('{0}{1}'.format(ALERT + '[!]' + END, e.code))
        return robot_urls

    except urllib.error.URLError as e:
        if DEBUG:
            print('{0}{1}'.format(ALERT + '[!]' + END, e.code))
        return robot_urls


if __name__ == "__main__":
    while cmd != 'q'.lower():
        # display menu and get cmd
        print('\nenter a command:')
        print('set | set url of site')
        print('q | kill session')
        cmd = input('==> ')

        if cmd == 'set'.lower():
            try:
                if config.URL and config.URL.strip() != '':
                    base_url = config.URL
                else:
                    base_url = input('URL==> ')
            except:
                base_url = input('URL==> ')

            print(SUCCESS + '[+]' + END + 'URL set')
            print(NOTICE + '[#]' + END + 'checking robots.txt')
            get_robot_urls(base_url)

        elif cmd == 'q'.lower():
            print(NOTICE + '[XXX]' + END + ',.-\'*^GAME_OVER^*\'-.,')

        else:
            print(ALERT + '[!]' + END + 'INVALID COMMAND')
