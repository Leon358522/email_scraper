import re
from selenium import webdriver

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
EDGE_DRIVER = './edgedriver_win64/msedgedriver'
DRIVER = webdriver.Edge(EDGE_DRIVER)


def get_emails(source: str):
    list_of_emails = []
    #  Used to recognise emails in text

    for re_match in re.finditer(EMAIL_REGEX, source):
        list_of_emails.append(re_match.group())

    return list_of_emails


def scrape_emails(url):
    DRIVER.get(url)
    page_source = DRIVER.page_source

    #  A function that returns all the emails from any Website

    return get_emails(page_source)


if __name__ == '__main__':
    sites = ['https://www.randomlists.com/email-addresses?qty=50', 'https://www.randomlists.com/email-addresses?qty=20']
    mails = []
    for site in sites:
        mails.append(scrape_emails(site))
    for i, mails in enumerate(mails):
        var = {f'{sites.__getitem__(i)}: {mails}'}
        print(var)
    DRIVER.close()
