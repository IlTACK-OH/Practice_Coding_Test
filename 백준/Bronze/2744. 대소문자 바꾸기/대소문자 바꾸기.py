in_str = input()
out_str = [i.lower() if i.isupper() else i.upper() for i in in_str]
print("".join(out_str))