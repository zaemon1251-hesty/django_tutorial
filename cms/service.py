import markdown


def get_html_from_text(text: str) -> str:
    """get html from text

    Args:
        text (str): text following the markdown rule

    Returns:
        str: html5 format generated from the text
    """
    return markdown.markdown(text, extensions=['fenced_code'])
