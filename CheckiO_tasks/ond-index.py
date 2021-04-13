def second_index(text: str, symbol: str) -> [int, None]:
    text = list(text)
    if symbol in text:
        text[text.index(symbol)] = ""
        if symbol in text:
            return text.index(symbol)
    return None


print(second_index("sims", "s"))