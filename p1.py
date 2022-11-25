mydict={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sep':54}
print("dictionary valuses ",mydict.values())
newlist=list()
for i in mydict.values():
    if i not in newlist:
        newlist.append(i)
        print("unique list",newlist)
