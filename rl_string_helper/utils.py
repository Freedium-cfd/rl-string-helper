import re

QUOTE_PATTERN = re.compile(r"""([&<>"'])(?!(amp|lt|gt|quot|#39);)""")
QUOTE_REPLACE_WITH = {
    "<": "&lt;",
    ">": "&gt;",
    "&": "&amp;",
    '"': "&quot;",  # should be escaped in attributes
    "'": "&#39",  # should be escaped in attributes
}

EXTRA_QUOTE_PATTERN = re.compile("|".join(map(re.escape, ["\n", "\t"])))  # '  '
EXTRA_QUOTE_REPLACE_WITH = {"\n": "<br />", "\t": "&emsp;", "  ": " &nbsp;"}


# https://stackoverflow.com/questions/1061697/whats-the-easiest-way-to-escape-html-in-python
def quote_html(html: str, extra: bool = True) -> str:
    for m in QUOTE_PATTERN.finditer(html):
        yield m.span(), QUOTE_REPLACE_WITH[m.group(1)]
    if extra:
        for m in EXTRA_QUOTE_PATTERN.finditer(html):
            pos = m.span()
            yield pos, EXTRA_QUOTE_REPLACE_WITH[html[pos[0]:pos[1]]]
