def fn_append(ale: set):
    ale_copy = ale.copy()
    ale_copy.add("😍😍😍😍😍😍😍😍😍")
    print(ale_copy)


container = {10, "😊", True, None}
print(container)
fn_append(container)
print(container)
