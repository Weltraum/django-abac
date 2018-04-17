# Django ABAC (Attribute-based access control)

Модель контроля доступа к объектам, основанная на анализе правил для атрибутов
объектов или субъектов, возможных операций с ними и окружения,
соответствующего запросу.
<br/>[Wikipedia](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0_%D0%BD%D0%B0_%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B5_%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%BE%D0%B2)
<br/>[Habrahabr](https://habrahabr.ru/company/custis/blog/248649/)

### Quick start

1. Add "abac" to your INSTALLED_APPS setting like this::
``` python
    INSTALLED_APPS = [
        ...
        'abac',
    ]
```

## Оглавление
1. Quick start
1. [Settings](settings.md)
1. [Project architecture](project_architecture.md)
1. [Authentication](authentication.md)
1. [Rules](rules.md)
1. [Combining algorithms](algorithm.md)