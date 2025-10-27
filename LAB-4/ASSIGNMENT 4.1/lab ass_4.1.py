import re

def is_indian_mobile(number: str) -> bool:
    """
    Returns True if the given number is a valid Indian mobile number.
    Accepts formats like:
      - 10 digits starting with 6-9 (e.g., 9296252532)
      - With country code +91 or 91 (e.g., +919296252532, 919296252532)
      - With leading 0 (e.g., 09296252532)
      - Allows spaces or hyphens as separators
    """
    if not isinstance(number, str):
        return False

    # Remove spaces and hyphens
    cleaned = re.sub(r"[ \-]", "", number)

    # Valid patterns:
    #  - 10 digits starting with 6-9
    #  - Optional +91 or 91 or 0 prefix before the 10 digits
    pattern = re.compile(r"^(?:\+?91|0)?[6-9]\d{9}$")
    return bool(pattern.match(cleaned))


# Examples
if __name__ == "__main__":
    tests = [
        "9296252532",
        "+919296252532",
        "919296252532",
    ]
    for t in tests:
        print(t, "->", is_indian_mobile(t))