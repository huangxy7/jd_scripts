import time
import re

def main():
    timestamp = int(time.time()*1000)
    message = f"<!-- {timestamp} -->"
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub('<!-- START -->([\s\S]*?)<!-- END -->',
                     f'<!-- START -->\n{message}\n<!-- END -->', content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    main()