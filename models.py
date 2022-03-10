import random

class NaiveModel():
    def __init__(self, seq, gens, entropy):
        self.seq = seq
        self.gens = int(gens)
        self.entropy = int(entropy)

    def get_mutations(self):
        self.seqs = [self.seq]
        for i in range(self.gens):
            ns = []
            for m in self.seqs:
                for c in self.make_children(m):
                    ns.append(c)
            self.seqs = ns
        return self.seqs[1:]

    def make_children(self, m):
        c1 = []
        c2 = []
        for n in m:
            if random.random() < self.entropy / 10 ** 6:
                c1.append(random.choice(['A','C','T','G',''])) # todo: add insertions, add weights
            else:
                c1.append(n)
        for n in m:
            if random.random() < self.entropy / 10 ** 6:
                c2.append(random.choice(['A','C','T','G','']))
            else:
                c2.append(n)
        c1 = ''.join(c1)
        c2 = ''.join(c2)
        return (c1, c2)
