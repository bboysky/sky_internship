
def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()


def run_formula(dv, param=None):

    alpha135 = dv.add_formula("alpha135", "SMA(Delay(close/Delay(close,{}),{}),{},{})".format(20,1,20,1),is_quarterly=False,register_funcs={"SMA":SMA})

    return alpha135