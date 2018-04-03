# Combining algorithms

С комбинационными алгоритмами можно познакомиться в стандарте
[XACML](http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268)

Из него на данный момент реализовано 4:

### deny_overrides

### permit_overrides

### deny_unless_permit

### permit_unless_deny

                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
----------------------|----------------------|----------------------|----------------------|----------------------|
       permit         |       permit         |        deny          |       permit         |       permit         |
        deny          |        deny          |        deny          |        deny          |        deny          |
   not_applicable     |       permit         |        deny          |       permit         |       permit         |
    indeterminate     |       permit         |        deny          |       permit         |       permit         |

## Оглавление
1. [Quick start](index.md)
1. [Project architecture](project_architecture.md)
1. [Authentication](authentication.md)
1. [Rules](rules.md)
1. Combining algorithms