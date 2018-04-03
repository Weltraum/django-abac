# Combining algorithms

С комбинационными алгоритмами можно познакомиться в стандарте
[XACML](http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268)

Из него на данный момент реализовано 4:

### PERMIT_UNLESS_DENY

|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |
|      **deny**        |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |
| **not_applicable**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |
|  **indeterminate**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |

### DENY_UNLESS_PERMIT

|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |<span style="color:green">permit</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |
|      **deny**        |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |
| **not_applicable**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |
|  **indeterminate**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |

### PERMIT_OVERRIDES

|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |<span style="color:green">permit</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |<span style="color:green">permit</span> |
|      **deny**        |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:blue">indeterminate</span> |
| **not_applicable**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> | <span>not_applicable</span>   |<span style="color:blue">indeterminate</span> |
|  **indeterminate**   |<span style="color:green">permit</span> |<span style="color:blue">indeterminate</span> |<span style="color:blue">indeterminate</span> |<span style="color:blue">indeterminate</span> |

### DENY_OVERRIDES

|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |<span style="color:green">permit</span> |<span style="color:red">deny</span> |<span style="color:green">permit</span> |<span style="color:blue">indeterminate</span> |
|      **deny**        |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |<span style="color:red">deny</span> |
| **not_applicable**   |<span style="color:green">permit</span> |<span style="color:red">deny</span> | <span>not_applicable</span>   |<span style="color:blue">indeterminate</span> |
|  **indeterminate**   |<span style="color:blue">indeterminate</span> |<span style="color:red">deny</span> |<span style="color:blue">indeterminate</span> |<span style="color:blue">indeterminate</span> |



## Оглавление
1. [Quick start](index.md)
1. [Project architecture](project_architecture.md)
1. [Authentication](authentication.md)
1. [Rules](rules.md)
1. Combining algorithms