url = 'https://omnieq.com/underlyings/ARCA/SPY/chain/2021/04/09'
spy = pd.read_html(url)[0]
spy_price = 401  # TODO: Replace with closing 'SPY' Price
strikes = list(range(int(round(spy_price, 0))-10, int(round(spy_price, 0))+11))
d = {}
for opt in spy.itertuples():
    str_pri = int(opt.Strike)
    if str_pri in strikes:
        s = opt.Type
        d[f'SPY_{s}_{str_pri}'] = {
            'closingPrice': opt.Last,
            'side': opt.Type,
            'strikePrice': opt.Strike,
            'openInterest': opt.OI,
            'impVol': opt.IV,
            'gamma': opt.Gamma}

ge = {}

for key, val in d.items():
    exp = ge.get(val['strikePrice'], 0)
    t = val['side']
    gex = int(round(val['openInterest'] * 100 * val['gamma'], 0))
    if t.upper() == 'CALL':
        ge[val['strikePrice']] = exp + gex
    elif t.upper() == 'PUT':
        ge[val['strikePrice']] = exp - gex

    print(gex)
print(OrderedDict(sorted(ge.items())))
