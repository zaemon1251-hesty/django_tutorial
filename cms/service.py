import markdown

md = markdown.Markdown()


def get_html_from_text(text: str) -> str:
    """get html from text

    Args:
        text (str): text following the markdown rule

    Returns:
        str: html5 format generated from the text
    """
    return md.reset().convert(text, extensions=['fenced_code'])
