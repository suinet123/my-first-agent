def calculate_discount(price, percent):
    """Return the price after applying a percentage discount.

    Example: calculate_discount(100, 20) should return 80.0
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    discount = price * percent / 100
    return price + discount


if __name__ == "__main__":
    print(calculate_discount(100, 20))
