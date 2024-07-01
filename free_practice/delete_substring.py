def replace_repet(origin: str, sub: str) -> str:
    size = len(sub) - 1
    origin = origin
    mutable = list(origin)
    index = 0
    remove = 0

    while origin.find(sub, index):
        place = origin.find(sub, index)
        del mutable[place - remove]
        index += (size + 1)
        remove += 1

    result = str(mutable)
    return result


origin = "aabbccXXddXXeeffXXXXgg"
print(origin, replace_repet(origin, "XX"))
