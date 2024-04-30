import re

def check_string(string):
    country_code = "^(\+?7[\s-]?|8[\s-]?)?"
    operator_code = "(\d{3}|\(\d{3}\))"
    separator = "([\s-]?)"
    phone_number = country_code + operator_code + separator + "\d{3}" + separator + "\d{2}" + "\\4" + "\d{2}$"
    phone_number_pattern = re.compile(phone_number)

    symbols = "([^@]+)"
    ending = "(\.\w{2,}$)"
    email = symbols + "@" + symbols + ending

    phone_number_pattern = re.compile(phone_number)
    email_pattern = re.compile(email)

    if phone_number_pattern.match(string) or email_pattern.match(string):
        return True
    return False

# valid_phone_numbers = [
#     "89160000000",
#     "+79160000000",
#     "9160000000",
#     "8(916)000-00-00",
#     "+7(916)000-00-00",
#     "(916)000-00-00",
#     "8 (916) 000-00-00",
#     "+7 (916) 000-00-00",
#     "(916) 000-00-00",
#     "8(916)0000000",
#     "+7(916)0000000",
#     "(916)0000000",
#     "8-916-000-00-00",
#     "+7-916-000-00-00",
#     "916-000-00-00"
# ]

# for phone_number in valid_phone_numbers:
#     print(check_string(phone_number))

# -----------------------------------------------------

# valid_emails = [
#     "abc@abc.ab",
#     "abc@abc.ab.ab",
#     "a@ab.ab",
#     "abc.abc@abc.abc"
# ]

# invalid_emails = [
#     "@abc.abc",
#     "abc@abc",
#     "abc@abc.a",
#     "abc@abc.abc.a",
#     "abc@abc.",
#     "abc@abc@abc"
# ]

# for email in valid_emails:
#     print(check_string(email))

# for email in invalid_emails:
#     print(check_string(email))
