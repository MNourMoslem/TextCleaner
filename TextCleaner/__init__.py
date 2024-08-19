from . import _utils

STOP_WORDS = _utils.STOP_WORDS

def remove_numbers(text: str, sub_with: str = "") -> str:
    return _utils._remove_numbers(text=text, sub_with=sub_with)

def remove_non_alphanumerics(text: str, sub_with: str = "") -> str:
    return _utils._remove_non_alphanumerics(text=text, sub_with=sub_with)

def remove_emails(text: str, sub_with: str = "") -> str:
    return _utils._remove_emails(text=text, sub_with=sub_with)

def remove_wide_spaces(text: str, replace_with: str = " ", min_len: int = 2) -> str:
    return _utils._remove_wide_spaces(text=text, replace_with=replace_with, min_len=min_len)

def remove_urls(text: str, sub_with: str = "") -> str:
    return _utils._remove_urls(text=text, sub_with=sub_with)

def remove_tags(text: str, sub_with: str = "") -> str:
    return _utils._remove_tags(text=text, sub_with=sub_with)

def remove_repeated(text: str, sub_with: str = r"\1", min_len: int = 3) -> str:
    return _utils._remove_repeated(text=text, sub_with=sub_with, min_len=min_len)

def remove_stopwords(text: str, sub_with: str = "") -> str:
    return _utils._remove_stopwords(text=text, sub_with=sub_with)

def remove_hashtags(text: str, sub_with: str = "") -> str:
    return _utils._remove_hashtags(text=text, sub_with=sub_with)

def get_numbers(text: str) -> list:
    return _utils._get_numbers(text=text)

def get_non_alphanumeric(text: str) -> list:
    return _utils._get_non_alphanumeric(text=text)

def get_emails(text: str) -> list:
    return _utils._get_emails(text=text)

def get_urls(text: str) -> list:
    return _utils._get_urls(text=text)

def get_tags(text: str) -> list:
    return _utils._get_tags(text=text)

def get_hashtags(text: str) -> list:
    return _utils._get_hashtags(text=text)

def get_wordcount(text: str) -> int:
    return _utils._get_wordcount(text=text)

def get_charcount(text: str) -> int:
    return _utils._get_charcount(text=text)

def get_avgwordlength(text: str) -> float:
    return _utils._get_avgwordlength(text=text)

def get_stopwordscount(text: str) -> int:
    return _utils._get_stopwordscount(text=text)

