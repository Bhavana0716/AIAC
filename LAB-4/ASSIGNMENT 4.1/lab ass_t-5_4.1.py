import re
from collections import Counter

def most_frequent_word(paragraph: str) -> str:
    text = re.sub(r"[^\w\s]", "", paragraph.lower())
    counts = Counter(text.split())
    return max(counts, key=counts.get)

# Example 4
text4 = "i love python . python is easy language to learn. python is better than other languages."
print(most_frequent_word(text4))  # python