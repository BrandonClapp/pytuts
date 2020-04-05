from colorama import Fore, Back, Style, init

init()


def colored(foreground, background, text):
    print(foreground + background + text + Style.RESET_ALL)


colored(Fore.BLACK, Back.RED, "Not Authenticated")
colored(Fore.BLACK, Back.GREEN, "Authentication Successful")
