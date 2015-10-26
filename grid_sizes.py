import P15

for i in range(1, 21):
    paths = P15.enumerate_paths(i)
    print "{0}{1:=20}".format(i, paths)