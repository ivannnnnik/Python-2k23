# print('Hello, World!')
# hot keys
# 1. cmd + / - comment
# 2. cmd + c - copy
# 3. cmd + v - paste
# 4. cmd + shift + <-> - paste

type_int = 2
type_float = 2.0
type_str = "test"

converte_int_in_float = float(type_int)  # 2 --> 2.0
converte_float_in_int = int(type_float)  # 2.0 --> 2
# print(translate_float_in_int)
# print(translate_int_in_float)

a = 5
b = 10

a = a + b  # 15 # == a += b
a += b  # 25  # a = a + b

sum_a_b = a + b
mult_a_b = a * b
dev_a_b = a / b  # 2.5
int_dev_a_b = a // b  # 2

c = 49
degree = 10

deg_c = c ** degree  # Возведение в степень
test_c = c ** 1 / 2  # 1. 49 ** 1 ,а потом 49 / 2 == 24.5
sqrt_c = c ** (1 / 2)  # 1. 1 / 2 = 0.5, а потом 49 ** 0.5 == 7

# hierarchy: 1. () 2. ** 3. * and / 4. + and -
test_1 = (1 + 2 * 3) ** 2 - 5 / 10
# 1. 2 * 3 == 6 2. 6 + 1 = 7 3. 7 ** 2 = 49 4. 5 / 10 = 0.5 5. 49 - 0.5 = 48.5
print(test_1)

# 7 ** 1 = 7
# 7 ** 2 = 7 * 7

# print(sqrt_c)
# print(deg_c)
# print(mult_a_b)
# print(dev_a_b)
# print(int_dev_a_b)
