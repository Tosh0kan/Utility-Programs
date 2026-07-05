import argparse


prefixes = {
    'quetta': 10e30, 'ronna': 10e27, 'yotta': 10e24, 'zetta': 10e21,
    'exa': 10e18, 'peta': 10e15, 'tera': 10e12, 'giga': 10e9,
    'mega': 10e6, 'kilo': 10e3, 'hecto': 10e2, 'deca': 10e1, 'none': 10e0,
    'deci': 10e-1, 'centi': 10e-2, 'milli': 10e-3, 'micro': 10e-6,
    'nano': 10e-9, 'pico': 10e-12, 'femto': 10e-15, 'atto': 10e-18,
    'zepto': 10e-21, 'yocto': 10e-24
}


def si_conv (s_value:int, s_prefix: str, t_prefix: str) -> float:
    return s_value * (prefixes[s_prefix] / prefixes[t_prefix])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('s_value', type=int)
    parser.add_argument('s_prefix', type=str, default='none')
    parser.add_argument('t_prefix', type=str, default='none')
    args = parser.parse_args()
    print(f"{si_conv(args.s_value, args.s_prefix, args.t_prefix)} {args.t_prefix}")


if __name__ == '__main__':
    main()
