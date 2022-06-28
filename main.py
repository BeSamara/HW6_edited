import re

with open('MOCK_DATA.txt', 'r') as file:
    content = file.read()


def find_names():
    names = re.findall(r'([A-Z][A-Za-z-\']+)\s([A-Z][A-Za-z-\']+)', content)
    c = 0
    with open('names.txt', 'w') as f:
        for i in names:
            c += 1
            f.write(f'{c}. {i}\n')
    b = 0
    print(f'Fullname:')
    for i in names:
        b += 1
        print(f'{b}. {i}')

def find_emails():
    emails = re.findall(r'[A-Za-z0-9_-]+@[a-z.0-9]+', content)
    c = 0
    with open('emails.txt', 'w') as f:
        for i in emails:
            c += 1
            f.write(f'{c}. %s\n' % i)
    c = 0
    print('Emails:')
    for i in emails:
        c += 1
        print(f'{c}. {i}')

def find_file_names():
    file_names = re.findall(r'\s([A-Za-z0-9]+\.[A-Za-z0-9]{1,4})', content)
    b = 0
    with open('file_names.txt', 'w') as f:
        for i in file_names:
            b += 1
            f.write(f'{b}. %s\n' % i)
    c = 0
    print('File names:')
    for i in file_names:
        c += 1
        print(f'{c}. {i}')

def find_colors():
    codes = re.findall(r'\s#([a-z0-9]{6})\b', content)
    b = 0
    with open('color_codes.txt', 'w') as f:
        for i in codes:
            b += 1
            f.write(f'{b}. %s\n' % i)
    c = 0
    print('Color codes:')
    for i in codes:
        c += 1
        print(f'{c}. {i}')