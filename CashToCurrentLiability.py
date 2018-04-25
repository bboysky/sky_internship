def run_formula(dv):
    CashToCurrentLiability = dv.add_formula("CashToCurrentLiability",
               "TTM(cash_cash_equ_end_period)/tot_cur_liab"
               , is_quarterly=True)
    return CashToCurrentLiability