"""目标：定义一个 BankAccount 类，包含类变量 interest_rate 和实例变量 balance。
实现 deposit()、withdraw() 和 apply_interest() 方法。

提示：在类体内直接赋值的变量是类变量（所有实例共享）。
在 __init__ 中通过 self.xxx 赋值的是实例变量（每个实例独立拥有）。
修改类变量应通过 类名.变量名 进行。
注意：金额应使用 Decimal 类型，避免浮点数精度问题。
"""

from decimal import Decimal


class BankAccount:
    """表示一个银行账户。

    >>> BankAccount.interest_rate
    Decimal('0.03')
    >>> acc1 = BankAccount("小明")
    >>> acc1.deposit(Decimal('1000'))
    >>> acc1.balance
    Decimal('1000')
    >>> acc1.withdraw(Decimal('200'))
    True
    >>> acc1.balance
    Decimal('800')
    >>> acc1.withdraw(Decimal('2000'))
    False
    >>> acc1.balance
    Decimal('800')
    >>> acc1.apply_interest()
    >>> acc1.balance
    Decimal('824.00')
    >>> acc2 = BankAccount("小红")
    >>> acc2.deposit(Decimal('500'))
    >>> BankAccount.interest_rate = Decimal('0.05')
    >>> acc2.apply_interest()
    >>> acc2.balance
    Decimal('525.00')
    >>> BankAccount.interest_rate = Decimal('0.03')  # 恢复原值
    """

    interest_rate: Decimal = ...  # 类变量：年利率

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.balance: Decimal = ...  # 实例变量：余额，初始为 0

    def deposit(self, amount: Decimal) -> None:
        """存入金额，增加余额。"""
        raise NotImplementedError("代码未实现")

    def withdraw(self, amount: Decimal) -> bool:
        """取出金额，如果余额不足返回 False，否则返回 True。"""
        raise NotImplementedError("代码未实现")

    def apply_interest(self) -> None:
        """根据 interest_rate 计算利息并增加余额。
        利息 = 当前余额 × interest_rate
        """
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
