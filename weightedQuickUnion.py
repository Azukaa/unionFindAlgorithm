class WeightedQuickUnion:
    def __init__(self, n):
        self.n = int(n)
        self.objects = [obj for obj in range(0, self.n)]
        self.size = [obj for obj in range(0, self.n)]

    def __iter__(self):
        return iter(self.objects)

    def root(self, i):
        while i != self.objects[i]:
            i = self.objects[self.objects[i]]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)
        
        if self.size[pid] < self.size[qid]:
            self.objects[pid] = qid
            self.size[qid] += self.size[pid]
        else:
            self.objects[qid] = pid
            self.size[pid] += self.size[qid]

        return self.objects
