def myxml(tagname, content='', **kwargs):
    attr = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
    return f'<{tagname} {attr}>{content}</{tagname}'


print(myxml('foo','bar',a=1,b=2))