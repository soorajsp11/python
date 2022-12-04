from ast import operator
# F_bitwise operators
# bitwise operators in python are: AND(&), OR(|), XOR(^), NOT(~), left shift(<<),right shift(>>)

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print("0011 1100 & 0000 1101 =", c)

c = a | b;        # 61 = 0011 1101 
print("0011 1100 | 0000 1101 ==>", c)

c = a ^ b;        # 49 = 0011 0001
print("0011 1100 ^ 0000 1101 ==>", c)

c = ~a;           # -61 = 1100 0011
print("0011 1100 ~ ==>", c)

c = a << 2;       # 240 = 1111 0000
print("0011 1100 << ==>", c)

c = a >> 2;       # 15 = 0000 1111
print("0011 1100 >> ==>", c)
