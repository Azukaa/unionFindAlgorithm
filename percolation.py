from UnionFindAlgorithm import WeightedQuickUnion
import numpy


class Percolation:
    def __init__(self,n):
        "Creates an n by n grid with all sites initially blocked"
        if n<=0:
            raise ValueError("The value of n must be greater than 0")
        self.n  = n
        self.grid= numpy.zeros((self.n, self.n), dtype = int)
        self.structure = WeightedQuickUnion(self.n * self.n + 2)
        self.structureIsFull =  WeightedQuickUnion(self.n * self.n + 1)
        self.virtualTopSite = 0
        self.virtualbottomSite = self.n * self.n + 1
        self.openedGrid = 0
        



    def get_index_of_field_in_self_structure(self,row,col):
        " This method gets the equivalent index of the row[col] from the weighted union algorithm"
        return (row * self.n) + col+1

    def is_open(self, row, col):
        "Checks wether a site is open"
        return self.grid[row][col]

    def open(self,row,col):
        if not self.is_open(row,col):
            fieldIndex = self.get_index_of_field_in_self_structure(row,col)

            if row == 0:
                self.structure.union(self.virtualTopSite, fieldIndex)
            if row == self.n-1:
                self.structure.union(self.virtualbottomSite, fieldIndex)

            #Check up
            if row > 0 and  self.is_open(row-1, col):
                self.structure.union(fieldIndex, self.get_index_of_field_in_self_structure(row-1, col))

            #check down
            if row < self.n-1 and self.is_open(row + 1, col):
                self.structure.union(fieldIndex, self.get_index_of_field_in_self_structure(row + 1, col))
            #check left
            elif col > 0 and self.is_open(row, col-1):
                self.structure.union(fieldIndex, self.get_index_of_field_in_self_structure(row, col-1))

            #Check for right
            elif col < 0 and self.is_open(row, col+1):
                self.structure.union(fieldIndex, self.get_index_of_field_in_self_structure(row, col+1))

            self.grid[row][col] = 1
            self.openedGrid += 1
            return self.grid

    def is_full(self, row, col):
        "checks if sites are connected to the top/virtual top"
        return self.structure.connected(self.get_index_of_field_in_self_structure(row,col),self.virtualTopSite)


    def num_of_sites_opened(self):
        "Returns the number of opened site"
        return self.openedGrid

    def percolates(self):
        return self.structure.connected(self.virtualTopSite, self.virtualbottomSite )
