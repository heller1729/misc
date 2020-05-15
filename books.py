l=[('Harry Potter',35,1997),
   ('Lord Of The Rings',16,1954),
   ('Twilight',37,2005),
   ('The Subtle Art of not giving a f',27,2016),
   ('The Song Of Ice and Fire',47,1996)]
m=[]
for i in l:
    m.append((i[2],i[1],i[0]))
for i in m:
    print(i)