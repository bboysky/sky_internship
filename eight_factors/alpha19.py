def run_formula(dv, param=None):

    alpha19 = dv.add_formula("alpha19","If((close >= Delay(close,{}),(close-Delay(close,{}))/close),(close-Delay(close,{}))/Delay(close,{}))".format(5,5,5,5), is_quarterly=False)
    return alpha19