def run_formula(dv, param=None):
    sky_9 = dv.add_formula("sky_9",
                           "-(If((open>=close)&&(volume>=Delay(volume,{})),Log(high*volume),Log(low*Delay(volume,{}))))".format(1,1),
                           is_quarterly=False)
    return sky_9