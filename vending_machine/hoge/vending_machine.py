class VendingMachine:
    ALLOWED_MONEY_LIST = [10, 50, 100, 500, 1000]

    def check_insert_money(self, insert_money):
        """
        受け入れられる金額かどうかチェック
        """
        if insert_money not in self.ALLOWED_MONEY_LIST:
            return False
        return True
