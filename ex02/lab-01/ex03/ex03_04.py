def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    second_element = tuple_data[-1]
    return first_element, second_element

input_tuple = eval(input("nhap tuple: "))
fist, last = truy_cap_phan_tu(input_tuple)

print("phan tu dau tien : ", fist)
print("phan tu cuoi cung : ", last)
