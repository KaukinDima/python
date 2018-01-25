params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# print(params.items())

# print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))


s = ";".join(params)
print(s.split(";", 2))