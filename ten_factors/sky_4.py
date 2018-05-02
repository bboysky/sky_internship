def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()
def run_formula(dv, param=None):
    sky_4 = dv.add_formula('sky_4', '-(SMA(free_turnover_ratio - turnover_ratio,{},{}))'.format(3,1), is_quarterly=False,
                            register_funcs={"SMA": SMA})
    return sky_4