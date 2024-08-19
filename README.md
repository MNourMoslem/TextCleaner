# TextCleaner

This repository contains a set of text processing utility functions that help clean, extract, and manipulate textual data. The functions are defined in the __init__.py file, which imports the core logic from the _utils.py module.

Functions
1. remove_numbers(text: str, sub_with: str = "") -> str
Replaces all numeric characters in the input text with the specified sub_with string.

2. remove_non_alphanumerics(text: str, sub_with: str = "") -> str
Removes all non-alphanumeric characters (excluding spaces) from the input text and replaces them with the specified sub_with string.

3. remove_emails(text: str, sub_with: str = "") -> str
Identifies and removes email addresses from the input text, replacing them with the specified sub_with string.

4. remove_wide_spaces(text: str, replace_with: str = " ", min_len: int = 2) -> str
Replaces sequences of whitespace characters in the input text that are at least min_len characters long with the specified replace_with string.

5. remove_urls(text: str, sub_with: str = "") -> str
Identifies and removes URLs from the input text, replacing them with the specified sub_with string.

6. remove_tags(text: str, sub_with: str = "") -> str
Identifies and removes tags (starting with @) from the input text, replacing them with the specified sub_with string.

7. remove_repeated(text: str, sub_with: str = r"\1", min_len: int = 3) -> str
Removes characters repeated more than min_len times in sequence, replacing them with the specified sub_with string.

8. remove_stopwords(text: str, sub_with: str = "") -> str
Removes common stopwords from the input text, replacing them with the specified sub_with string.

9. remove_hashtags(text: str, sub_with: str = "") -> str
Identifies and removes hashtags (starting with #) from the input text, replacing them with the specified sub_with string.

10. get_numbers(text: str) -> list
Returns a list of all numeric sequences found in the input text.

11. get_non_alphanumeric(text: str) -> list
Returns a list of all non-alphanumeric characters (excluding spaces) found in the input text.

12. get_emails(text: str) -> list
Returns a list of all email addresses found in the input text.

13. get_urls(text: str) -> list
Returns a list of all URLs found in the input text.

14. get_tags(text: str) -> list
Returns a list of all tags (starting with @) found in the input text.

15. get_hashtags(text: str) -> list
Returns a list of all hashtags (starting with #) found in the input text.

16. get_wordcount(text: str) -> int
Returns the word count of the input text.

17. get_charcount(text: str) -> int
Returns the count of all non-space characters in the input text.

18. get_avgwordlength(text: str) -> float
Returns the average word length in the input text.

19. get_stopwordscount(text: str) -> int
Returns the count of all stopwords found in the input text.

