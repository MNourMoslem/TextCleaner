import regex
import re

STOP_WORDS = {'four', 'elsewhere', "'ve", 'of', 'whereupon', 'after', 'latterly', 'please', 'whence', 'whereafter',
              'few', 'hereafter', 'eight', '‘ve', 'onto', 'anyway', 'nobody', 'once', 'sixty', 'thereupon', 'full',
              'forty', '’m', 'be', 'thence', 'had', 'my', 'else', 'must', 'hers', 'twelve', 'only', 'during', 'ever',
              'just', 'herself', 'last', 'from', 'top', 'also', 'herein', 'upon', 'anyhow', 'which', 'ourselves', 'does',
              'beforehand', 'n’t', 'becomes', 'front', 'or', "'ll", 'an', '‘re', 'bottom', 'among', 'hence', 'keep', 'formerly',
              'across', 'amount', 'never', 'everyone', 'without', "'re", 'nothing', 'into', 'quite', 'six', 'whom', 'off', 'he',
              'several', 'yourself', 'make', 'such', 'other', 'move', 'put', "'s", 'someone', '‘d', 'meanwhile', 'now', 'i',
              'another', 'serious', 'this', 'did', 'himself', "'d", '’ve', 'its', 'nine', 'indeed', 'see', '’ll', 'yours',
              'therein', 'who', 'often', 'became', 'via', 'except', 'but', 'most', 'under', 'throughout', 'because', 'take',
              'has', 'every', 'former', 'down', 'two', 'still', 'eleven', 'toward', 'anyone', 'latter', '‘s', 'always', 'him',
              'those', 'these', 'than', 'wherever', 'wherein', 're', 'name', 'some', 'is', 'due', 'against', 'using', 'out',
              'hereby', 'around', 'the', 'too', 'whoever', 'various', 'amongst', 'there', 'above', 'mine', 'five', 'as', 'perhaps',
              'go', 'already', 'next', 'noone', 'everything', 'whither', 'well', 'a', 'whereas', 'myself', 'why', 'somewhere',
              'further', 'their', 'may', 'very', 'n‘t', 'thereby', 'all', 'on', 'them', 'ten', 'your', 'it', 'we', 'at', 'should',
              'themselves', 'three', 'was', 'unless', 'am', 'whatever', 'somehow', 'are', 'nevertheless', 'something', 'less', 'seem',
              'almost', 'none', 'what', 'regarding', 'besides', 'although', 'have', 'by', 'her', 'empty', 'then', 'whether', 'show',
              'in', 'sometimes', 'might', 'made', 'really', 'us', 'for', 'thus', 'though', 'between', 'seems', 'however', 'whereby',
              'through', 'towards', 'per', "n't", 'over', 'anything', 'enough', 'itself', 'back', 'thru', 'done', 'whole', 'any', 'again',
              'and', 'behind', 'being', 'sometime', 'up', 'twenty', 'ca', '’re', 'beside', 'here', 'his', 'hundred', 'seeming', 'ours',
              'where', 'until', 'alone', 'before', 'own', 'others', 'yet', 'afterwards', 'whose', 'been', 'same', 'while', 'moreover', '’s',
              'everywhere', 'how', 'yourselves', 'many', 'hereupon', 'doing', 'neither', 'each', 'get', 'even', 'nowhere', 'beyond', 'could',
              'one', 'side', '’d', 'rather', 'would', 'together', 'below', 'were', 'within', 'since', 'become', 'third', 'to', 'call', 'therefore',
              'first', 'do', 'that', 'can', '‘ll', 'along', 'becoming', 'whenever', 'either', 'they', 'no', 'cannot', 'give', 'used', 'fifteen', 'say',
              'least', 'will', 'both', 'thereafter', 'mostly', 'you', 'not', 'part', 'namely', 'nor', 'fifty', 'about', 'so', 'otherwise', 'when', "'m",
              'me', 'anywhere', 'our', 'more', 'much', 'seemed', '‘m', 'she', 'if', 'with'}

def _remove_numbers(text : str, sub_with : str = "") -> str:
  return regex.sub("[\d]+", sub_with, text)

def _remove_non_alphanumerics(text : str, sub_with : str = "") -> str:
  return regex.sub("[^\s\w]+", sub_with, text)

def _remove_emails(text : str, sub_with : str = "") -> str:
  return regex.sub("\w+@\w+\.\w+", sub_with, text)

def _remove_wide_spaces(text : str, replce_with : str = " ", min_len = 2) -> str:
  return regex.sub("\s{%d,}" % min_len, replce_with, text)

def _remove_urls(text : str, sub_with : str = "") -> str:
  return regex.sub(r"(?:https://)?(?:www\.)?\w+\.\w+(?:\.\w+)?", sub_with, text)

def _remove_tags(text : str, sub_with : str = "") -> str:
  return regex.sub("@[^\s]+", sub_with, text)

def _remove_repeated(text : str, sub_with : str = r"\1", min_len = 3) -> str:
  return re.sub(r"([^\d\W])\1{%d,}" % min_len, sub_with, text)

def _remove_stopwords(text : str, sub_with : str  = "") -> str:
  return regex.sub(r"\b(?:{})\b".format("|".join(STOP_WORDS)), sub_with, text)

def _remove_hashtags(text : str, sub_with : str  = "") -> str:
  return regex.sub(r"#[^\s]*", sub_with, text)

def _get_numbers(text : str) -> list:
  return regex.findall("[\d]+", text)

def _get_non_alphanumeric(text : str) -> list:
  return regex.findall("[^\s\w]+", text)

def _get_emails(text : str) -> list:
  return regex.findall("\w+@\w+\.\w+", text)

def _get_urls(text : str) -> list:
  return regex.findall(r"(?:https://)?(?:www\.)?\w+\.\w+(?:\.\w+)??", text)

def _get_tags(text : str) -> list:
  return regex.findall("@[^\s]+", text)

def _get_hashtags(text : str) -> list:
  return regex.findall(r"#[^\s]*", text)

def _get_wordcount(text : str) -> int:
  return len(regex.findall("[\s]+", text.strip())) + 1 

def _get_charcount(text : str)-> int:
  return len(regex.findall("[^\s]", text.strip()))

def _get_avgwordlength(text : str) -> float:
  return _get_charcount(text) / _get_wordcount(text)

def _get_stopwordscount(text : str) -> int:
  return len(regex.findall(r"\b(?:{})\b".format("|".join(STOP_WORDS)), text))
