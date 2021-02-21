# set, himpunan : tidak mementingkan urutan

# superhero = {"wiro sableng",
#             "gundala","gatot",
#             "habibie & ainun",
#             "negeri 5 menara"}

# superhero.add("mak lampir")
# superhero.add("gundala")

superhero = set()

superhero.add("muhammad")
superhero.add("umar")
superhero.add("ali")
superhero.add("utsman")
superhero.add(1435)

print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(prima))