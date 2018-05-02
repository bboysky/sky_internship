def run_formula(dv, param=None):
    sky_3 = dv.add_formula('sky_3',
                           '-(Max(high-low,Max(Abs(high-Delay(close,{})),Abs(Delay(close,{})-low)))*(Max(volume,Delay(volume,{}))))'.format(1,1,1),
                           is_quarterly=False)
    return sky_3