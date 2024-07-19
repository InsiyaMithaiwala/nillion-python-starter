from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the difference between my_int1 and my_int2, then square the result
    difference = my_int1 - my_int2
    final_result = difference * difference

    return [Output(final_result, "my_output", party1)]
