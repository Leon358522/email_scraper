import re

#  Used to recognise emails in text
email_regex = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


#  A function that returns all the emails from any String
def get_emails(source: str):
    list_of_emails = []

    for re_match in re.finditer(email_regex, source):
        list_of_emails.append(re_match.group())

    return list_of_emails


#  Sample text
text = "This is a sample text. There are emails like: apple@gmail.com, and google@apple.com"
text2 = "it can be confusing, but any email works: mario.luigi@gmail.com (peach_bowser@toad.com)"
sample_text = text + text2

#  Grabbing the emails from the sample text
emails = get_emails(sample_text)
print(emails)
