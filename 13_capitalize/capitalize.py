def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    out = ''
    li = list(phrase)
    li[0] = li[0].upper()
    print(li)
    newStr = out.join(li)
    return newStr



   