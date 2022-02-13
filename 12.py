str = "8"*70

while "2222" in str or "8888" in str:
    if "2222" in str:
        str.replace("2222", "88")
    else: str.replace("8888", "22")

print(str)

