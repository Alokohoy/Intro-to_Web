import re

text = "Call me at 555-1234 or at the office line 555-5678. For emergencies, dial 555-9999."
pattern = r"\d{3}-\d{4}"
phone_numbers = re.findall(pattern, text)
print("Phone Numbers Found:", phone_numbers)


#task 2

import re

text = "Hello, world! Welcome to regex."
text2 = "Greetings! Hello, how are you?"

pattern = r"Hello"

match1 = re.match(pattern, text)
print("Using re.match() on text:")
if match1:
    print("Match found:", match1.group())
else:
    print("No match found.")

match2 = re.match(pattern, text2)
print("\nUsing re.match() on text2:")
if match2:
    print("Match found:", match2.group())
else:
    print("No match found.")

search_result = re.search(pattern, text2)
print("\nUsing re.search() on text2:")
if search_result:
    print("Found:", search_result.group())
else:
    print("No match found.")

#task 3

import re

text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."
pattern = r"\d+"
result = re.sub(pattern, "NUMBER", text)
print("Modified text:", result)

#task 4
import re

text = "For more info, contact us at support@example.com or sales-info@example.org"

pattern = r"\b\w+@\w+\.\w+\b"

emails = re.findall(pattern, text)

print("Emails found:", emails)

#task 5

import re

text = "An apple a day keeps the doctor away. Even elephants enjoy eating oranges."

pattern = r"\b[aeiou]\w*\b"

words_starting_with_vowel = re.findall(pattern, text, re.IGNORECASE)

print("Words starting with a vowel:", words_starting_with_vowel)



