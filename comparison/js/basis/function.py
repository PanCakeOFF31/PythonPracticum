from helpers import print_section


def showMessage(message: str = 'Message') -> None:
    print(message)
    pass


#
def program_1():
    print_section("program_1(): ")
    showMessage()
    showMessage('Super message')
    pass


#
program_1()
