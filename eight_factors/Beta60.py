def run_formula(dv):
    Bata60 = dv.add_formula("Bata60",
                            "Covariance(benchmark_ret(),stock_data(),{})/(StdDev(benchmark_ret(),{}))^{})".format(60,60,2)
                            , is_quarterly=False,register_funcs={"benchmark_ret":benchmark_ret,"stock_data":stock_data})
    return Bata60


def stock_data():
    stock_data = dv.get_ts('close').pct_change()
    return stock_data

def benchmark_ret():
    ben = ds.index_daily(['000300.SH'],start,end,'close')[0]
    ben_close = np.array(ben['close'])
    stock_d = dv.get_ts('close').pct.change()
    benchmark = {}
    for i in stock_d.columns:
        benchmark[i] = ben_close
    benchmark_ret = pd.DataFrame(data = benchmark,index = stock_d.index).pct_change()
    return benchmark_ret