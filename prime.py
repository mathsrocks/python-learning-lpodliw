def check_if_prime(number_to_check):
    for x in range(2, number_to_check):
        if number_to_check % x == 0:
            return False
    return True
