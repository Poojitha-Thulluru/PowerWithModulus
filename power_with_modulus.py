def get_power_modulus(given_base: int, given_power: int, given_divisor: int) -> int:
    given_base = given_base % given_divisor
    output = 1
    for val in range(1, given_divisor + 1):
        output = (output * given_base) % given_divisor
    return output % given_divisor


try:
    base = int(input("Enter Base : "))
    power = int(input("Enter power : "))
    divisor = int(input("Enter divisor : "))
    print(f"Therefore, {base} ^ {power} % {divisor} = ", get_power_modulus(base, power, divisor))
except ValueError:
    print("Invalid Input. Please Enter only integers")