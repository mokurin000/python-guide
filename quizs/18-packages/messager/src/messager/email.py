def send(to: str, subject: str, body: str) -> str:
    """发送邮件（模拟）。

    >>> send("alice@example.com", "你好", "Hello!")
    '发送邮件到 alice@example.com：你好'
    """
    return f"发送邮件到 {to}：{subject}"
