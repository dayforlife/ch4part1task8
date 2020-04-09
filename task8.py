import moneyfmt

cash = moneyfmt.MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
repr(cash)