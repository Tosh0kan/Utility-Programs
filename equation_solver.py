import argparse

import sympy
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

def main() -> None:
    sympy
    transformations = standard_transformations + (implicit_multiplication_application,) + (convert_xor,)

    parser = argparse.ArgumentParser()
    parser.add_argument("equation", help="Your equation must be adjusted so it's equal to zero.",
                        type=str, default=False)
    args = parser.parse_args()
    if args.equation:
        equation_list = list(args.equation)
        for e in equation_list:
            if e.isalpha():
                exec(f"{e} = sympy.symbols('{e}')")
        expr = parse_expr(args.equation, transformations=transformations)
        solution = sympy.solve(expr.evalf())
        solution = [round(n,5) for n in solution]
        print(solution)

if __name__ == "__main__":
    main()
