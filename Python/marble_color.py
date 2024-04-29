def marble_color(text, color):
    """
    Apply color to the given text for terminal output.

    Parameters:
        text (str): The text to be colorized.
        color (str): The color to apply to the text. Available colors are 
            'blue', 'yellow', 'green', 'red', 'white', and 'black'.

    Returns:
        str: The colorized text string suitable for terminal output.
    """
    colors = {
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'red': '\033[91m',
        'white': '\033[0m',
        'black': '\033[30m'
    }
    color_code = colors.get(color.lower())
    if color_code:
        return f"{color_code}{text}\033[0m"
    else:
        return text
