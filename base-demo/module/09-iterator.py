from itertools import product, permutations, combinations

# 笛卡尔积
cartesian_product = list(product([1, 2], ['a', 'b']))
print(f"笛卡尔积: {cartesian_product}")

# 排列
word_permutations = list(permutations('ABC'))
print(f"排列: {word_permutations}")

# 组合
letter_combinations = list(combinations('ABCD', 2))
print(f"组合: {letter_combinations}")