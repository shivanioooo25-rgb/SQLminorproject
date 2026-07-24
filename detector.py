import re

patterns = [

    r"(?i)(OR|AND)\s+\d+\s*=\s*\d+",

    r"(?i)UNION\s+SELECT",

    r"(?i)DROP\s+TABLE",

    r"(?i)SELECT\s+\*",

    r"(--|#|'|;)"

]

def detect_sql_injection(user_input):

    for pattern in patterns:

        if re.search(pattern, user_input):

            return True

    return False