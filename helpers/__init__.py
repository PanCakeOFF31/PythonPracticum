ARTICLE_LINE = '======================================================================'
SECTION_LINE = '----------------------------------------------------------------------'
SUB_SECTION_LINE = '-----------------------------------'


def print_article(message: str = None):
    print(ARTICLE_LINE)
    if message is not None:
        print('\t\t\t', message)


def print_article_ending():
    print(ARTICLE_LINE)


def print_section(message: str = None):
    print(SECTION_LINE)
    if message is not None:
        print('\t\t', message)


def print_section_ending():
    print(SECTION_LINE)


def print_subsection(message: str = None):
    print(SUB_SECTION_LINE)
    if message is not None:
        print('\t', message)


def print_subsection_ending():
    print(SUB_SECTION_LINE)


def log(message: str = None):
    print(SUB_SECTION_LINE)
    if message is not None:
        print('\t', message)


def log_info(message: str = None):
    print(SUB_SECTION_LINE)
    if message is not None:
        print(message)
