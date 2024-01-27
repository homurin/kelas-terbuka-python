# asterisk args or *args

def sum(*number: int):
    results = 0
    for i in number:
        results += i
    return results


print(sum(1, 2, 3, 4, 5,))


# kwargs

def createHTML(tag: str, text: str, **attr: str):
    html = f'<{tag}'
    for key, val in attr.items():
        html += f' {key}="{val}" '
    html += f'>{text}</{tag}>'
    return html


print(createHTML('h1', 'hello world', className='mt-5'))

# case study


def Math(*number: float, **option: str):
    results = 0
    if (option.get('method') == 'add'):
        for i in number:
            results += i
    elif (option.get('method') == 'multiply'):
        results = 1
        for i in number:
            results *= i
    else:
        print('no operation')
    return results


print(Math(1, 2, 3, 4, 5, method="add"))
print(Math(1, 2, 3, 4, 5, method="multiply"))
