MONEY_LIST = [10, 50, 100, 500, 1000]


def check_insert_money(insert_money):
    if insert_money not in MONEY_LIST:
        return False
    return True
