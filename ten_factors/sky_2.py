def run_formula(dv, param=None):
    sky_2 = dv.add_formula('sky_2',
                           "-(Max(close-Delay(close,{}),Max(close-Delay(close,{}),Max(close-Delay(close,{}),Max(close-Delay(close,{}),close-Delay(close,{}))))))".format(1,2,3,4,5)
                           , is_quarterly=False)
    return sky_2