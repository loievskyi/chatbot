def save_to_db(exchange_rates: dict):
    pass


def format_output(exchange_rates: dict):
    try:
        output = []
        for name, value in exchange_rates['rates'].items():
            output.append(f"{name}: {value:.2f}")
        return "\n".join(output)
    except Exception as ex:
        return str(ex)
