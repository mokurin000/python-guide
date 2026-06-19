"""目标：掌握 json 模块的序列化和反序列化。

使用 json.dumps() 和 json.loads() 完成以下任务。

提示：
- `json.dumps(obj, indent=N, ensure_ascii=False)` 序列化为字符串
- `json.loads(s)` 将 JSON 字符串解析为 Python 对象
- 使用 `ensure_ascii=False` 保留非 ASCII 字符（如中文）
- 使用 `indent=2` 或 `indent=4` 美化输出
"""

import json


def serialize_to_json(data: dict, indent: int = 2) -> str:
    """将字典序列化为格式化的 JSON 字符串。

    >>> result = serialize_to_json({"name": "Alice", "age": 30})
    >>> print(result)
    {
      "name": "Alice",
      "age": 30
    }
    """
    raise NotImplementedError("代码未实现")


def serialize_with_chinese(data: dict) -> str:
    """将包含中文的字典序列化为 JSON 字符串，确保中文不被转义。

    >>> result = serialize_with_chinese({"name": "张三", "city": "北京"})
    >>> "张三" in result
    True
    >>> "\\\\u" not in result
    True
    """
    raise NotImplementedError("代码未实现")


def deserialize_from_json(s: str) -> dict:
    """将 JSON 字符串解析为 Python 字典。

    >>> deserialize_from_json('{"name": "Alice", "age": 30}')
    {'name': 'Alice', 'age': 30}
    >>> deserialize_from_json('{"scores": [88, 92, 85]}')
    {'scores': [88, 92, 85]}
    >>> deserialize_from_json('{"valid": true, "count": null}')
    {'valid': True, 'count': None}
    """
    raise NotImplementedError("代码未实现")


def update_and_serialize(data: dict, key: str, value) -> str:
    """向字典中添加键值对，然后序列化为格式化的 JSON。

    >>> result = update_and_serialize({"name": "Alice"}, "age", 30)
    >>> "Alice" in result and "30" in result
    True
    >>> result2 = update_and_serialize({"x": 1}, "y", 2)
    >>> '"x"' in result2 and '"y"' in result2
    True
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
