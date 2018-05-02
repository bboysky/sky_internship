def run_formula(dv, param=None):
    sky_1 = dv.add_formula('sky_1', "-Correlation(Return(Log(close),{}),Log(volume),{})".format(1,20), is_quarterly=False)
    return sky_1