import markdown

# markdown extension configuration
md_extensions = ['abbr', 'fenced_code', 'tables']


def get_html_from_text(text: str) -> str:
    """get html from text

    Args:
        text (str): text following the markdown rule

    Returns:
        str: html5 format generated from the text
    """
    return markdown.markdown(
        text, extensions=md_extensions
    )
