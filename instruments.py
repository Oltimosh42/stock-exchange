def get_instruments():
    return ["SBER", "GAZP", "LKOH"]

def is_valid_symbol(symbol):
    return bool(symbol.strip())

if __name__ == "__main__":
    print(get_instruments())
    assert is_valid_symbol("SBER")
    assert not is_valid_symbol("    ")
    print("Проверка символов пройдена")
