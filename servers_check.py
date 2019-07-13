from os import system

up_msg = "Server Is Up & Running!"
down_msg = "Server Is Down!"

# all servers dict
servers = {}
servers['Brand_Group'] = '198.143.179.197'
# servers['TedX_UI'] = '198.143.179.118'

ping_cmd = "ping -c 1 {0}"


def server_checker():

    for key, value in servers.items():
        print("\033[35m\033[1mStart Checking {0} Server\033[21m\033[0m".format(key))
        status = system(ping_cmd.format(value))

        if status == 0:
            print("\033[92m\033[1m{0} {1} \033[21m\033[0m\n".format(key, up_msg))
        else:
            print("\033[31m\033[1m{0} {1} \033[21m\033[0m\n".format(key, down_msg))

    return True


server_checker()
