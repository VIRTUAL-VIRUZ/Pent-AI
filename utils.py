
import re

def parse_html(html):
    return re.findall('<title>(.*?)</title>', html)
