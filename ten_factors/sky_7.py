def run_formula(dv, param=None):
    sky_7 = dv.add_formula("sky_7", "-(Ewma(Rank(Correlation(vwap,volume,{})),{}))".format(5,5), is_quarterly=False)
    return sky_7