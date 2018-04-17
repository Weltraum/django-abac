# Settings

#### DEFAULT_AUTHENTICATION
Настройка определяет, использует ли ABAC стандартную аутификацию
прописанную в настройках **MIDDLEWARE** Django. По умолчанию True.
Если вы хотите, использовать собственную аунтификацию к ресурсам,
к которым ограничен доступ с помощью ABAC, необходимо прописать их в
ADDITIONAL_AUTHENTICATION_CLASS

```python
ABAC_SETTINGS = {
    'DEFAULT_AUTHENTICATION': True,
}
```

#### ADDITIONAL_AUTHENTICATION_CLASS
В данную настройку помещаются дополнительные классы аутификации. В ABAC
уже подготовленны некоторые дополнительные классы аунтификации,
импользуемые в REST Framework (не забудьте его добавить в проект):

```python
ABAC_SETTINGS = {
    'ADDITIONAL_AUTHENTICATION_CLASS': (
        'abac.authentication.RestFrameworkBasicAuthentication',
        'abac.authentication.RestFrameworkSessionAuthentication',
        'abac.authentication.RestFrameworkTokenAuthentication',
        'abac.authentication.RestFrameworkRemoteUserAuthentication',
        'abac.authentication.RestFrameworkJSONWebTokenAuthentication',
    ),
}
```

Как создать собственный класс аунтификации для ABAC смотрите в разделе
???

#### CACHE_RULE_TIMEOUT
Время жизни вычислений в правилах и политиках ABAC. По умолчанию 3 секунды.

```python
ABAC_SETTINGS = {
    'CACHE_RULE_TIMEOUT': 3,
}
```

#### EXPRESSIONS
Список всех возможных выражений для правил и политик, отмеченные
декоратором @expression

#### PARSER
Словарь парсеров файлов правил и политик, в качестве ключей которого
выступают расширение файлов. Добавляются с помошью декоратора @parser.
По умоланию потдерживаются json файлы.

```python
ABAC_SETTINGS = {
    'PARSER': {'.json': json.loads},
}
```

## Оглавление
1. [Quick start](index.md)
1. Settings
1. [Project architecture](project_architecture.md)
1. [Authentication](authentication.md)
1. [Rules](rules.md)
1. [Combining algorithms](algorithm.md)