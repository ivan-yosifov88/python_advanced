class NameTooShortError():
    """
    When the name is less then 4 characters
    """
    pass


class MustContainAtSymbolError(Exception):
    """
    When email do not contain @
    """

    pass


class InvalidDomainError(Exception):
    """
    When domain is different from .com, .bg, ,org, .net
    """

    pass


data = input()

while not data == "End":
    valid_domains = [".com", ".bg", ".org", ".net"]
    if "@" not in data:
        raise MustContainAtSymbolError("Email must contain @")
    user, site = data.split("@")
    if len(user) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    _, domain = site.split(".")
    domain = f".{domain}"
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid" )

    data = input()