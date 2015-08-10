#!/usr/bin/env python
#title           :  permutations.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 9, 2015
#version         :  1.0
#usage           :  python permutations.py
#notes           :  This script is a permuations puzzle from codewars
#python_version  :  2.7

import unittest
class Permuations(unittest.TestCase):

    def permutation(self, data):
        temp = ''
        bank = set()
        letters = []
        results = []

        for letter in data:
            letters.append(letter)
            bank.add(letter)

        print "letters = " + str(letters)
        print "bank = " + str(bank) + "\n"

        if len(letters) == 1:
            return letters

        index = len(letters)
        print "index = " + str(index)

        tempLetters = letters[:]

        for i in range(0, index):
            print "i = " + str(i)
            temp += letters[i]
            tempLetters.pop(i)

            remaining = len(tempLetters)

            while remaining > -1:


                remaining -= 1
            for item in tempLetters:
                temp += item

            print temp
            results.append(temp)
            print "temp after = " + temp
            print "letters = " + str(letters)
            temp = ''
            tempLetters = letters[:]
            print "tempLetters = " + str(tempLetters) + '\n'

        # for i in range(0, index):
        #         print "i = " + str(i)
        #         temp += letters[i]
        #         print "temp before = " + temp
        #
        #         for item in letters:
        #             if item is not letters[i]:
        #                 temp += item
        #         results.append(temp)
        #         print "temp after = " + temp
        #         temp = ''

        for item in results:
            print "results = " + str(results)
            print "item = " + str(item)

            for i in range(0, len(item)):
                print "item[i] = " + item[i]

                print "item.count(item[i]) = " + str(item.count(item[i]))
                print "data.count(item[i]) = " + str(data.count(item[i]))

                if item.count(item[i]) > data.count(item[i]):
                    results.remove(item)
                    print "results = " + str(results)
                    print "end for item in results \n"
                    break


        print results
        print ''
        results = list(set(results))
        print results
        return results

    def stuff(self, data):
        print "data = " + str(data)
        if len(data) == 1:
            return list(data)
        else:
            for i in range(0, len(data)):
                data[i] + str(self.stuff(data[1:]))

#++++++++++++++++++++++++++++++++TESTING +++++++++++++++++++++++++++++++++++#
    def test(self):
        print "Stuff 1"
        self.assertEqual(self.stuff('a'), ['a']);

        print "Stuff 2"
        self.assertEqual(self.stuff('ab'), ['ab', 'ba']);

        print "Test 1"
        self.assertEqual(self.permutation('a'), ['a']);
        print "Test 2"
        self.assertEqual(self.permutation('ab'), ['ab', 'ba']);
        print "Test 3"
        self.assertEqual(self.permutation('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']);
if __name__ == '__main__':
    unittest.main()
