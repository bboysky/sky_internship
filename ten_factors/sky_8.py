def run_formula(dv, param=None):
    sky_8 = dv.add_formula("sky_8", "-(Rank(Covariance(Rank(Ts_Mean(volume,{})),Ts_Mean(Rank(close),{}),{})))".format(5,5,5),
                           is_quarterly=False)
    return sky_8