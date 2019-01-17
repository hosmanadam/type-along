import termcolor


def bold(text):
    return termcolor.colored(text, attrs=['bold'])


def dark(text):
    return termcolor.colored(text, attrs=['dark'])


def red(text):
    return termcolor.colored(text, color='red')


def green(text):
    return termcolor.colored(text, color='green')
