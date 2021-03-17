def symbols_counter(text_line, symbols_dict):
    for symbol in text_line:
        if symbol not in symbols_dict:
            symbols_dict[symbol] = 0
        symbols_dict[symbol] += 1


def print_sort_result(symbols_dict):
    sorted_symbols_dict = sorted(symbols_dict.items())
    for symbol, count in sorted_symbols_dict:
        print(f"{symbol}: {count} time/s")


text = input()

symbols = {}

symbols_counter(text, symbols)

print_sort_result(symbols)