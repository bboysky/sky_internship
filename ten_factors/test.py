import pandas as pd

def get_dv(start=20170101, end=20180101):
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService

    import warnings

    warnings.filterwarnings("ignore")

    # --------------------------------------------------------

    # define
    factor_list = ['np_parent_comp_ttm', 'tot_cur_liab', 'cogstosales', 'oper_rev_ttm', 'tangibleasset', 'interestdebt']
    check_factor = ','.join(factor_list)

    dataview_folder = r'd:/data'
    ds = LocalDataService(fp=dataview_folder)

    ZZ800_id = ds.query_index_member("000906.SH", start, end)
    stock_symbol = list(set(ZZ800_id))

    ben_ret = list(ds.index_daily(['000300.SH'], start, end, 'close'))[0]

    dv_props = {'start_date': start, 'end_date': end, 'symbol': ','.join(stock_symbol),
                'fields': check_factor,
                'freq': 1,
                "prepare_fields": True}

    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()
    return dv


if 'dv' not in dir():
    dv = get_dv()


# ---------------------------------------------------------
# test output
def test(factor, data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date', 'report_date'] and columns_name == 'symbol'):
                raise NameError(
                    '''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')

        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str

        if columns_dtype not in ['object', 'str']:
            raise TypeError('error columns type')

        if index_dtype not in ['int32', 'int64', 'int']:
            raise TypeError('error index type')
        print('{} OK!'.format(factor))


from ten_factors import sky_1, sky_2, sky_3,sky_4, sky_5, sky_6, sky_7,sky_8,sky_9,sky_10

for f in ['sky_1', 'sky_2', 'sky_3','sky_4','sky_5','sky_6','sky_7','sky_8','sky_9','sky_10']:
    test(f, globals()[f].run_formula(dv))