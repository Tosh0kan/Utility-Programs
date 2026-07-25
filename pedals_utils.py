import os
import sys
import argparse 

from PySide6.QtCore import (
    QSize,
    Qt
)

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QComboBox
)

prefixes = {
    'quetta': 1e30, 'ronna': 1e27, 'yotta': 1e24, 'zetta': 1e21,
    'exa': 1e18, 'peta': 1e15, 'tera': 1e12, 'giga': 1e9,
    'mega': 1e6, 'kilo': 1e3, 'hecto': 1e2, 'deca': 1e1, 'none': 1e0,
    'deci': 1e-1, 'centi': 1e-2, 'milli': 1e-3, 'micro': 1e-6,
    'nano': 1e-9, 'pico': 1e-12, 'femto': 1e-15, 'atto': 1e-18,
    'zepto': 1e-21, 'yocto': 1e-24
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DIYPedals Swiss Army Knife')

        menu_s_prefix = QComboBox()
        menu_t_prefix = QComboBox()
        for key, value in prefixes.items():
            menu_s_prefix.addItem(key)
            menu_t_prefix.addItem(key)
        self.setCentralWidget(menu_s_prefix)


def si_conv (s_value:float, s_prefix: str, t_prefix: str) -> float:
    raw_result = s_value * (prefixes[s_prefix] / prefixes[t_prefix])
    return float(f"{raw_result:.15g}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('s_value', type=float)
    parser.add_argument('s_prefix', type=str, default='none')
    parser.add_argument('t_prefix', type=str, default='none')
    parser.add_argument('-g', '--gui', action='store_true')
    args = parser.parse_args()
    print(args.s_value, args.s_prefix, args.t_prefix)

    if args.gui:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()

    else:
        print(f"{si_conv(args.s_value, args.s_prefix, args.t_prefix)} {args.t_prefix}")


if __name__ == '__main__':
    main()
