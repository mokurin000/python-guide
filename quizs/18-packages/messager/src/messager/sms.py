def send(phone: str, message: str) -> str:
    """发送短信（模拟）。

    >>> send("13800138000", "包的概念很简单")
    '发送短信到 13800138000：包的概念很简单'
    """
    return f"发送短信到 {phone}：{message}"
