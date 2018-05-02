def run_formula(dv):
    SalesCostRatio = dv.add_formula("SalesCostRatio",
               "TTM(tot_oper_cost)/TTM(oper_rev)"
               , is_quarterly=True)
    return SalesCostRatio