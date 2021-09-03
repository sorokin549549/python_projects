num = int(input())
bin_num = bin(num)  # 0b1111111
oct_num = oct(num)  # 0o177
hex_num = hex(num).upper()  # 0x7f

print(bin_num[2:])  # 1111111
print(oct_num[2:])  # 177
print(hex_num[2:])