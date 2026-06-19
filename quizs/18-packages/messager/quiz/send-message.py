"""目标：从真实的包中导入并使用模块。

本练习使用 `messager` 包（位于本项目的 `src/messager/` 目录下）。
你可以先查看它的结构：

```
messager/
├── src/messager/
│   ├── __init__.py   # 重新导出 send_email 和 send_sms
│   ├── email.py      # 提供 send(to, subject, body) 函数
│   └── sms.py        # 提供 send(phone, message) 函数
```

请确保在 `messager/` 目录下运行本文件：
    uv run python quiz/send-message.py
"""


def send_email_via_module() -> str:
    """导入 messager.email 模块，调用它的 send 函数发送邮件。

    使用 `import messager.email` 方式，然后通过完整路径调用。

    >>> result = send_email_via_module()
    >>> result
    '发送邮件到 alice@example.com：会议提醒'
    """
    raise NotImplementedError("代码未实现")


def send_sms_via_from_import() -> str:
    """从 messager.sms 中直接导入 send 函数，发送短信。

    使用 `from messager.sms import send` 方式。

    >>> result = send_sms_via_from_import()
    >>> result
    '发送短信到 13800138000：晚上一起吃饭吗？'
    """
    raise NotImplementedError("代码未实现")


def send_email_via_init() -> str:
    """从 messager 包直接导入 send_email（由 __init__.py 重新导出）。

    使用 `from messager import send_email`。

    >>> result = send_email_via_init()
    >>> result
    '发送邮件到 bob@example.com：项目更新'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
