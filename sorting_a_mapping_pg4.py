# # #program 4 - sorting a dictionary
# #wap to sort a dictionary by key

x = {"ariana_grande": 250, "justin_bieber": 200e+100, 'lady_gaga': 100, 'dj_snake': 100e+12}

y = sorted(x.keys())

z = dict()

for i in y:
    z[i] = x[i]
print(z)
