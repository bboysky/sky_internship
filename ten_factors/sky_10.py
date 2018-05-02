def run_formula(dv, param=None):
    sky_10 = dv.add_formula('sky_10',"-(Ta('TRIMA',0,(close-Delay(close,1))/close,"
                                     "(close-Delay(close,1))/close,(close-Delay(close,1))/close,"
                                     "(close-Delay(close,1))/close,(close-Delay(close,1))/close,30))".format(1,1,1,1,1,30)
                            , is_quarterly=False)
    return sky_10