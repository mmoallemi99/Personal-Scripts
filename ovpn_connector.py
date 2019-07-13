from os import listdir, getcwd, system
from os.path import isfile, join
import sys


passed_args = sys.argv

if passed_args[-1].isdigit():
    number_of_tries = int(passed_args[-1])
else:
    number_of_tries = -1


def get_config_files():

    current_path = getcwd()
    all_files_folders = listdir(current_path)
    just_files = []
    
    for item in all_files_folders:
        if isfile(join(current_path, item)):
            just_files.append(item)
    
    just_files.reverse()
    return just_files


def openvpn(config_files):
    print("\033[92m\033[1mConnecting To OpenVPN\033[21m\033[0m\n")
    bash_command = "sudo openvpn --auth-nocache --config '{0}'"
    for index, config in enumerate(config_files):
        if number_of_tries == index:
            return
        print("\033[35m\033[1mTrying {0}\033[21m\033[0m\n".format(config))
        system(bash_command.format(config))
        print("\033[31m\033[1m{0} IS {1}\033[21m\033[0m\n".format(config, "DISCONNECTED!"))


def tor_openvpn(config_files):
    print("\033[92m\033[1mConnect To OpenVPN Through Tor\033[21m\033[0m\n")
    bash_command = "sudo proxychains -q openvpn --auth-nocache --config '{0}'"
    for index, config in enumerate(config_files):
        if number_of_tries == index:
            return
        print("\033[35m\033[1mTrying {0}\033[21m\033[0m\n".format(config))
        system(bash_command.format(config))
        print("\033[31m\033[1m{0} IS {1}\033[21m\033[0m\n".format(config, "DISCONNECTED!"))


if 'tor' in passed_args:
    config_files = get_config_files()
    tor_openvpn(config_files)
else:
    config_files = get_config_files()
    openvpn(config_files)
