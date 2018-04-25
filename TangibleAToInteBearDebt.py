def run_formula(dv):
    TangibleAToInteBearDebt = dv.add_formula("TangibleAToInteBearDebt",
               "tangibleasset/interestdebt"
               , is_quarterly=False)
    return TangibleAToInteBearDebt