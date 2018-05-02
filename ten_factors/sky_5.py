def run_formula(dv, param=None):
    sky_5 = dv.add_formula('sky_5', 'Ts_Sum(free_turnover_ratio*({}-free_turnover_ratio)*close,{})/{}'.format(1,5,5), is_quarterly=False)
    return sky_5