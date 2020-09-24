money_list = [10, 50, 100, 500, 1000]


def get_input_money(input_money):
    if input_money not in money_list:
        return "想定外の投入金額です"
    return input_money


# 【Vending Machineの機能】10円、100円、XX
## テスト内容:指定された金額は受け入れて、それ以外はErrorを起こすテスト
def test_valid_money():
    """
    正しい金額が設定されていることを確認するテスト関数
    """
    input_money = 100
    # 自販機の入力金額を読み取る関数を設置
    input_money = get_input_money(input_money)
    assert input_money in money_list


def test_invalid_money():
    """
    不正の金額が設定されていることを確認するテスト関数
    """
    input_money = 200
    # 自販機の入力金額を読み取る関数を設置
    input_money = get_input_money(input_money)
    assert input_money == "想定外の投入金額です"


# 投入・投入金額の総計
# 複数回メソッドを呼べるようにする。入れた回数分お金を集計できているかテスト


# 払い戻しXX
# 払い戻しができるかテスト、投入金額の数値が返ってくるかテスト

