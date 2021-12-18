import re


def validate_email(email: str):
    return re.match(pattern=r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", string=email)


def if_have_symbols(line: str):
    return re.match(pattern=r"[^A-Za-z0-9]", string=line)
