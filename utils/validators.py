import ipaddress
import re


def validate_target(target):

    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        pass

    domain_regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

    if re.match(domain_regex, target):
        return True

    return False