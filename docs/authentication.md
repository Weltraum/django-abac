# Аунтификация пользователей

## Настройка
Если Вы использует стандартные механизмы аунтификаци в Django,
то достаточно присвоить ключю 'DEFAULT_AUTHENTICATION'
значение True, либо ничего не указывать, так как это значение
по умолчанию:

```python
ABAC_SETTINGS = {
    'DEFAULT_AUTHENTICATION': True,
}
```
Если Вы используете не стандартные механизмы аунтификации,
такие как аунтификацию из модулей rest-framework или
rest-framework-jwt, то их необходимо перечислить в поле
'ADDITIONAL_AUTHENTICATION_CLASS':
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
Модуль Django-abac уже предоставляет дополнительные классы
аунтификации, используемые в rest-framework и
rest-framework-jwt, а так же предоставляет возможность 
подключить собственные классы.

Заметьте, что настройки 'DEFAULT_AUTHENTICATION' и 
'ADDITIONAL_AUTHENTICATION_CLASS' могут использоваться одновременно.

## Создание собственных классов аунтификации
От класса аунтификации ожидается, что она содержит
функции authenticate которая принимает request и возвращает
класс пользователя унаследованного от
django.contrib.auth.models.AbstractUser. А в случае неудачи,
бросает исключение AbacAuthenticationFailed.
```python
from abac.exception import AbacAuthenticationFailed

class MyAuthenticationClass:

    def authenticate(self, request):
        user = my_get_user(request)
        if user.is_authenticated:
            return user
        else:
            raise AbacAuthenticationFailed(msg)
```
