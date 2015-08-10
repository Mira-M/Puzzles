#!/usr/bin/env python
#title           :  sudoku.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 9, 2015
#version         :  1.0
#usage           :  python sudoku.py
#notes           :  This script is a sudoku puzzle from codewars
#python_version  :  2.7

import unittest
class SudokuTest(unittest.TestCase):

    def sudoku(self, a):

        compact = []
        for item in a:
            compact.extend(item)

        a = ''.join(str(e) for e in compact)

        solution = self.solve(a)

        print "solution = " + str(solution)

        return str(solution)

    def solve(self, a):
        if len(a) != 81:
            print "Incorrect string length"


        i = a.find('0')
        # print "i = " + str(i)
        if i == -1:
            return a

        excluded_numbers = set()
        for j in range(81):
            if self.same_row(i,j) or self.same_col(i,j) or self.same_block(i,j):
                excluded_numbers.add(a[j])

        print "excluded_numbers = " + str(excluded_numbers)
        for m in '123456789':
            if m not in excluded_numbers:
                self.solve(a[:i]+m+a[i+1:])

    def same_row(self,i,j): return (i/9 == j/9)
    def same_col(self,i,j): return (i-j) % 9 == 0
    def same_block(self,i,j): return (i/27 == j/27 and i%9/3 == j%9/3)


#++++++++++++++++++++++++++++++++TESTING +++++++++++++++++++++++++++++++++++#
    def test(self):
        puzzle = [[5,3,0,0,7,0,0,0,0],
                  [6,3,0,1,9,5,0,0,0],
                  [0,9,8,0,0,0,0,6,0],
                  [8,0,0,0,6,0,0,0,3],
                  [4,0,0,8,0,3,0,0,1],
                  [7,0,0,0,2,0,0,0,6],
                  [0,6,0,0,0,0,2,8,0],
                  [0,0,0,4,1,9,0,0,5],
                  [0,0,0,0,8,0,0,7,9]]

        solution = [[5,3,4,6,7,8,9,1,2],
                    [6,7,2,1,9,5,3,4,8],
                    [1,9,8,3,4,2,5,6,7],
                    [8,5,9,7,6,1,4,2,3],
                    [4,2,6,8,5,3,7,9,1],
                    [7,1,3,9,2,4,8,5,6],
                    [9,6,1,5,3,7,2,8,4],
                    [2,8,7,4,1,9,6,3,5],
                    [3,4,5,2,8,6,1,7,9]]

        self.assertEqual(self.sudoku(puzzle), solution, "Incorrect solution");

if __name__ == '__main__':
    unittest.main()
