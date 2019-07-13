import os
import socket

CONNECTED_MSG = "Tor Is Connected!"
NOT_CONNECTED_MSG = "Not Connected!"


def tor_reset():
    """
    resets tor client
    """
    FAILED_MSG = "Something Went Wrong With Restarting Tor\nTrying Again!"
    reset_tor = "sudo systemctl restart tor"
    status = os.system(reset_tor)
    # print(status)
    # if not status:
    #     print("\033[31m\033[1m{0}\033[21m\033[0m\n".format(FAILED_MSG))
    #     tor_reset()


def connection_checker():
    """
    checks whether it can connect to tor network with pinging tor's website
    """
    ENV_PROXY = "socks5://127.0.0.1:9050"
    PROXY_CMD = "export all_proxy=\"{0}\""
    os.system(PROXY_CMD.format(ENV_PROXY))
    TOR_WEBSITE = "torproject.org"

    print("\033[35m\033[1mStart Checking Tor Website\033[21m\033[0m")

    while True:
        try:
            socket.create_connection((TOR_WEBSITE, 80))
            print("\033[92m\033[1m{0}\033[21m\033[0m\n".format(CONNECTED_MSG))
            return
        except ConnectionRefusedError:
            tor_reset()

    # if status:
    #     print("\033[92m\033[1m{0}\033[21m\033[0m\n".format(CONNECTED_MSG))
    # else:
    #     tor_reset()


connection_checker()
