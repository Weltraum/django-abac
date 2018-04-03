# Combining algorithms

С комбинационными алгоритмами можно познакомиться в стандарте
[XACML](http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268)

Из него на данный момент реализовано 4:

### PERMIT_UNLESS_DENY

|                      |       <span style="color:green">permit</span>         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |       permit         |        deny          |       permit         |       permit         |
|      **deny**        |        deny          |        deny          |        deny          |        deny          |
| **not_applicable**   |       permit         |        deny          |       permit         |       permit         |
|  **indeterminate**   |       permit         |        deny          |       permit         |       permit         |

### DENY_UNLESS_PERMIT
|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |       permit         |       permit         |       permit         |       permit         |
|      **deny**        |       permit         |        deny          |        deny          |        deny          |
| **not_applicable**   |       permit         |        deny          |        deny          |        deny          |
|  **indeterminate**   |       permit         |        deny          |        deny          |        deny          |

### PERMIT_OVERRIDES
|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |       permit         |       permit         |       permit         |       permit         |
|      **deny**        |       permit         |        deny          |        deny          |    indeterminate     |
| **not_applicable**   |       permit         |        deny          |   not_applicable     |    indeterminate     |
|  **indeterminate**   |       permit         |    indeterminate     |    indeterminate     |    indeterminate     |

### DENY_OVERRIDES
|                      |       permit         |        deny          |   not_applicable     |    indeterminate     |
|----------------------|----------------------|----------------------|----------------------|----------------------|
|     **permit**       |       permit         |        deny          |       permit         |    indeterminate     |
|      **deny**        |        deny          |        deny          |        deny          |        deny          |
| **not_applicable**   |       permit         |        deny          |   not_applicable     |    indeterminate     |
|  **indeterminate**   |    indeterminate     |        deny          |    indeterminate     |    indeterminate     |

Some Markdown text with <span style="color:blue">some *blue* text</span>

## Оглавление
1. [Quick start](index.md)
1. [Project architecture](project_architecture.md)
1. [Authentication](authentication.md)
1. [Rules](rules.md)
1. Combining algorithms