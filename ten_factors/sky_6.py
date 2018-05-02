def run_formula(dv, param=None):
    sky_6 = dv.add_formula("sky_6", "-(Percentile(Ta('MA',0,(high-low),(high-low),(high-low),(high-low),{})))".format(5),
                           is_quarterly=False)
    return sky_6