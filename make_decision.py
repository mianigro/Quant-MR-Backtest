def make_decision(z_score):
    if z_score >= 2.0:
        trade_option = "Long"

    elif z_score <= -2.0:
        trade_option = "Short"

    else:
        trade_option = None

    return trade_option

