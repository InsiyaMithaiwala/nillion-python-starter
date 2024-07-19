from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the greatest common divisor (GCD) of my_int1 and my_int2
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcd_result = SecretInteger(gcd(my_int1, my_int2))

    return [Output(gcd_result, "my_output", party1)]
