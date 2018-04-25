def run_formula(dv, param=None):

    MA10Close = dv.add_formula("MA10Close", "Ta('MA',0,close,close,close,close,10)/close" ,
                        is_quarterly=False)
    return MA10Close