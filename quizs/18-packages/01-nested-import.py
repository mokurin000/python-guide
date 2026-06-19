"""目标：理解包中的模块导入。

在包中，模块通过层级结构组织。本练习模拟一个简单的包结构：

messenger/
├── __init__.py
├── email.py
└── sms.py

请实现以下函数，模拟不同导入方式下的访问路径。
"""


def import_top_level(package_name: str) -> str:
    """返回导入顶级包后，访问其中 email 模块的写法。

    例如，import messenger 后，访问 email 模块的方式是 messenger.email。

    >>> import_top_level("messenger")
    'messenger.email'
    >>> import_top_level("mypackage")
    'mypackage.email'
    """
    raise NotImplementedError("代码未实现")


def from_submodule(module_name: str, func_name: str) -> str:
    """返回使用 from ... import ... 导入子模块中函数的写法。

    例如，from messenger.email import send，返回 'send'。

    >>> from_submodule("messenger.email", "send")
    'send'
    >>> from_submodule("messenger.sms", "send")
    'send'
    """
    raise NotImplementedError("代码未实现")


def import_with_alias(module_name: str, alias: str) -> str:
    """返回导入模块并起别名的写法。

    例如，import messenger.email as mail，返回 'mail'。

    >>> import_with_alias("messenger.email", "mail")
    'mail'
    >>> import_with_alias("messenger.sms", "text")
    'text'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
