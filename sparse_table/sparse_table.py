from math import floor, log2

class MinSparseTable:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.p = floor(log2(self.n) / log2(2))
        self.table = [[0] * (self.n) for _ in range(self.p+1)]
        self.indices = [[0] * (self.n) for _ in range(self.p+1)]
        self.logs = [0] * (self.n+1)

        for i in range(self.n):
            self.table[0][i] = arr[i]
            self.indices[0][i] = i

        for i in range(2, self.n+1):
            self.logs[i] = self.logs[i//2]+1

        for i in range(1, self.p+1):
            j = 0
            while j + (1 << i) <= self.n:
                left = self.table[i-1][j]
                right = self.table[i-1][j+(1 << (i-1))]
                self.table[i][j] = min(left, right)

                if left <= right:
                    self.indices[i][j] = self.indices[i-1][j]
                else:
                    self.indices[i][j] = self.indices[i-1][j+(1 << (i-1))]
                j +=1

    def query(self, l: int, r: int) -> int:
        length = r - l + 1
        p = self.logs[length]
        k = 1 << p
        return min(self.table[p][l], self.table[p][r-k+1])
    
    def query_index(self, l: int, r: int) -> int:
        length = r - l + 1
        p = self.logs[length]
        k = 1 << p
        left = self.table[p][l]
        right = self.table[p][r-k+1]
        return self.indices[p][l] if left <= right else self.indices[p][r-k+1]
    
values = [1, 2, -3, 2, 4, -1, 5]
sparseTable = MinSparseTable(values)

print(sparseTable.query(1, 5)) # prints -3
print(sparseTable.query_index(1, 5)) # prints 2

print(sparseTable.query(3, 3)) # prints 2
print(sparseTable.query_index(3, 3)) # prints 3

print(sparseTable.query(3, 6)) # prints -1
print(sparseTable.query_index(3, 6)) # prints 5