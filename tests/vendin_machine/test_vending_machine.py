import pytest

from vending_machine.hoge.vending_machine import VendingMachine

# 自販機に金額を投入できることを確認するテスト
def test_insert_money():
    vending_machine = VendingMachine()
    vending_machine.insert(100)


# 【Vending Machineの機能】10円、100円、XX
## テスト内容:指定された金額は受け入れて、それ以外はErrorを起こすテスト
insert_money_list = [
    (10),
    (50),
    (100),
    (500),
    (1000),
]


@pytest.mark.parametrize("money", insert_money_list)
def test_valid_money(money):
    """
    正しい金額が設定されていることを確認するテスト関数
    """
    # 自販機の入力金額を読み取る関数を設置
    result = VendingMachine().check_insert_money(money)
    assert result


def test_invalid_money():
    """
    不正の金額が設定されていることを確認するテスト関数
    """
    insert_money = 200
    # 自販機の入力金額を読み取る関数を設置
    result = VendingMachine().check_insert_money(insert_money)
    assert not result


# 複数回投入
# 投入・投入金額の総計

# insert_money = [100,100]


# def test_get_num_money():
#     assert count(insert_mon)

# def test_get_total_money():
#     assert sum(insert_money)


# 複数回メソッドを呼べるようにする。入れた回数分お金を集計できているかテスト
##

# 払い戻しXX
# 払い戻しができるかテスト、投入金額の数値が返ってくるかテスト
