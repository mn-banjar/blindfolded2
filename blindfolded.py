#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename      : blindfolded.py
# Author        : Moneera Banjar
# Created       : Sat, 08 Aug 2020
# Last Modified : Wed, 12 Aug 2020


from sys import exit as Die
try:
    import sys
    import RubiksBlindfolded
    from video import webcam
except ImportError as err:
    Die(err)

    

def run():
    notation = {
            'blue'  : 'F',
            'white'  : 'U',
            'green'   : 'B',
            'orange'    : 'R',
            'red' : 'L',
            'yellow' : 'D'
        }
    
    state         = webcam.scan(notation)
    if not state:
        print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides.')
        print('Please try again.\033[0m')
        Die(1)
    
    
    from results import results
    RubiksBlindfolded.setCube(state)
    print(RubiksBlindfolded.displayCube())
    
    try:
        edge = RubiksBlindfolded.solveEdges()
        edgeIndex = RubiksBlindfolded.indexEdgeSequence()
        edgeBuffer = RubiksBlindfolded.currentEdgeBuffer()
        
        parity = RubiksBlindfolded.parityCheck()
        RubiksBlindfolded.parityAlgorithm()
        
        corner = RubiksBlindfolded.solveCorners()
        cornerIndex = RubiksBlindfolded.indexCornerSequence()
        cornerBuffer = RubiksBlindfolded.currentCornerBuffer()
        
        
    except Exception as err:
        print('\033[0;33m[QBR SOLVE ERROR] Ops, you did not scan in all 6 sides correctly.')
        print('Please try again.\033[0m')
        Die(1)

    print('-- SOLUTION --')
    print('Starting position:\n    front: blue\n    top: white\n')
    print('edge sequence:')
    print(edge)
    print('parity check {}'.format(parity))
    print('corner sequence:')
    print(corner)
    
    results.visualization(edgeIndex,cornerIndex,edgeBuffer,cornerBuffer,parity,notation)
    
    Die(0)
    
   

if __name__ == '__main__':
    run()    
