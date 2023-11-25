def is_valid_pin_codes(pin_codes):
    if len(set(pin_codes)) != len(pin_codes) or len(pin_codes) == 0:
        return False
    for i in pin_codes:
        try:
            int(i)
        except ValueError:
            return False
        if len(i) != 4:
            return False
    return True


print(is_valid_pin_codes(['1101', '9034', '00112']))
