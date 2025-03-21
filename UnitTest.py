###ETML
###Auteur : Mark Lovink
###Date : 30.05.2023
###Description : File use to perform unit test with the function that get the position between the rook and the king

#import Library 
import unittest

##### Summary
### This function is used to retrieve all the positions between the rook and the king when in check
##### Summary    
### Return a list with all the position
def getPositionsBetween( kingRow, kingCol, rookRow, rookCol):
        positionsBetween = []

        if kingRow == rookRow:
            if kingCol < rookCol:
                postionColBetween= 1  
            else:
                postionColBetween=-1

            col = kingCol + postionColBetween
            while col != rookCol:
                positionsBetween.append((kingRow, col))
                col += postionColBetween
        
        
        elif kingCol == rookCol:
            
            if kingRow < rookRow:
                postionRowBetween= 1  
            else:
                postionRowBetween=-1
            row = kingRow + postionRowBetween

            while row != rookRow:
                positionsBetween.append((row, kingCol))
                row += postionRowBetween

        return positionsBetween

class TestGetPositionsBetween(unittest.TestCase):
    ##### Summary
    ### This function is used to test the "getPositionsBetween" function when the king and the rook are on the same column
    ##### Summary  
    def testGetPositionsBetweenColumn(self):
        kingCol=4
        kingRow =2
        rookCol=4
        rookRow=7
        expectedPositions = [(3, 4), (4, 4), (5, 4),(6,4)]
        positions = getPositionsBetween(kingRow, kingCol, rookRow, rookCol)
        self.assertEqual(positions, expectedPositions)

    ##### Summary
    ### This function is used to test the "getPositionsBetween" function when the king and the rook are on the same row
    ##### Summary  
    def testGetPositionsBetweenRow(self):
        kingCol=5
        kingRow = 4
        rookCol=7
        rookRow = 4
        expectedPositions = [ (4, 6)]
        positions = getPositionsBetween(kingRow, kingCol, rookRow, rookCol)
        self.assertEqual(positions, expectedPositions)

    ##### Summary
    ### This function is used to test the "getPositionsBetween" function when the king and the rook are not on the same column or row
    ##### Summary  
    def testGetPositionsBetweenNothing(self):
        kingCol= 1
        kingRow= 1
        rookCol= 2
        rookRow = 3
        expectedPositions = []
        positions = getPositionsBetween(kingRow, kingCol, rookRow, rookCol)
        self.assertEqual(positions, expectedPositions)

#start the test
if __name__ == '__main__':
    unittest.main()