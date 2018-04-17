"""
Читаем файлы из директории
различаем тип файлов и используем свой конструктор
"""

import json
import os


def parse_rules_and_policy(file):
    _, extension = os.path.splitext(file.name)
    return PARSER[extension.lower()](file)


with open('../_development/sample/rule.json', 'r') as f:
    d = parse_rules_and_policy(f)


