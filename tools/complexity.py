# TODO use SC tag to compute sequence uniqueness
def sequence_uniqueness(gfa_fn):
    with open(gfa_fn) as f:
        for r in f:
            r = r.strip().split("\t")
            if r[0] != "L":
                continue
            n1 = int(r[1])
            n2 = int(r[3])
            weight = None
            for f in r[6:]:
                f = f.split(":")
                if f[0] == "SC":
                    weight = int(f[2])
            if weight == None:
                weight = 1
    pass # TODO