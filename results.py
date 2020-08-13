#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename      : results.py
# Author        : Moneera Banjar
# Created       : Mon, 03 Aug 2020
# Last Modified : Wed, 12 Aug 2020


from sys import exit as Die
import numpy as np 
import cv2 
from colordetection import ColorDetector
from sys import exit as Die
try:
    import sys
except ImportError as err:
    Die(err)
  


class Results:
    
    def __init__(self):
        self.cap              = cv2.VideoCapture(0)
    
    def visualization (self,edgeIndex,cornerIndex,edgeBuffer,cornerBuffer,parity,mainNotation):
        '''
        Draw cubes for edge and corner sequence, determine the currnet buffer with its colors 
        and the target of the cubie, the pink color on the target represents the swapped face
        the arrow keys use to flip and display the sequence
        
        :param edgeIndex: the edge index list from RubikBlindfolded package
        :param cornerIndex: the corner index list from RubikBlindfolded package
        :param edgeBuffer: the currnet buffer list from RubikBlindfolded package
        :param cornerBuffer: the currnet buffer list from RubikBlindfolded package
        '''
        
        edgeCounter = 0
        cornerCounter = 0
        current = 'edge'
        notation = {}
        
        
        while True:
            _, frame = self.cap.read()
            
            cv2.putText(frame, 'Edge Sequence', (20,40), cv2.FONT_HERSHEY_SIMPLEX ,
                        1, (50,50,50), 2, cv2.LINE_AA) 
            cv2.putText(frame, 'Corner Sequence', (20,280), cv2.FONT_HERSHEY_SIMPLEX ,
                        1, (50,50,50), 2, cv2.LINE_AA) 
            
            if (parity==0):
                cv2.putText(frame, 'Even Parity', (320,40), cv2.FONT_HERSHEY_SIMPLEX ,
                            0.5, (50,50,50), 2, cv2.LINE_AA)
            elif (parity==1):
                cv2.putText(frame, 'Odd Parity, apply parity algorithm', (320,40), cv2.FONT_HERSHEY_SIMPLEX ,
                            0.5, (50,50,50), 2, cv2.LINE_AA)
            #(B,G,R)
            
            
            whiteF = mainNotation['white'] 
            blueF = mainNotation['blue'] 
            orangeF = mainNotation['orange'] 
            yellowF = mainNotation['yellow'] 
            redF = mainNotation['red'] 
            greenF = mainNotation['green'] 
            
            notation[whiteF] =  'white'
            notation[blueF] =  'blue'
            notation[orangeF] =  'orange'
            notation[yellowF] =  'yellow'
            notation[redF] =  'red'
            notation[greenF] =  'green'
            
            #draw cube lines
            scale = 240
            for z in range(2):
                for m in range(6):
                    if (m == 0):
                        #U
                        scale1 = 20
                        scale2 = 6
                        scale3 = -20
                        scale4 = 6
                        xp = [100,120,140,120]
                        yp = [66,72,66,60]
                        
                    elif (m == 1):
                        #F
                        scale1 = 20
                        scale2 = 6
                        scale3 = 0
                        scale4 = 22
                        xp = [60,60,80,80]
                        yp = [78,100,106,84]
                        
                    elif (m == 2):
                        #R
                        scale1 = 20
                        scale2 = -6
                        scale3 = 0
                        scale4 = 22
                        xp = [120,120,140,140]
                        yp = [96,118,112,90]
                        
                    elif (m == 3):
                        #D
                        scale1 = 20
                        scale2 = 6
                        scale3 = 20
                        scale4 = -6
                        xp = [230,210,230,250]
                        yp = [138,144,150,144]
                        
                    elif (m == 4):
                        #L
                        scale1 = -20
                        scale2 = 6
                        scale3 = 0
                        scale4 = 22
                        xp = [270,250,250,270]
                        yp = [82,88,66,60]
                        
                    elif (m == 5):
                        #B
                        scale1 = -20
                        scale2 = -6
                        scale3 = 0
                        scale4 = 22
                        xp = [310,330,330,310]
                        yp = [94,100,78,72]
                    
                    
                    # x rows y columns
                    for x in range(3):
                        for y in range(3):
                            a1 = np.array( [[[xp[0]+(scale1*y)+(scale3*x),yp[0]+(scale2*y)+(scale4*x)+(scale*z)],
                                             [xp[1]+(scale1*y)+(scale3*x),yp[1]+(scale2*y)+(scale4*x)+(scale*z)],
                                             [xp[2]+(scale1*y)+(scale3*x),yp[2]+(scale2*y)+(scale4*x)+(scale*z)],
                                             [xp[3]+(scale1*y)+(scale3*x),yp[3]+(scale2*y)+(scale4*x)+(scale*z)]]],
                                           dtype=np.int32 )
                            if (x==1 and y==1):
                                if (m==0):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['U']) )
                                elif (m==1):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['F']) )
                                elif (m==2):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['R']) )
                                elif (m==3):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['D']) )
                                elif (m==4):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['L']) )
                                elif (m==5):
                                    cv2.fillPoly( frame, a1, ColorDetector.name_to_rgb(notation['B']) )
                            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            
            
                
                
            #draw edge sequence
            #counter
            if current=='edge':
                numColor = (80,80,80)
            elif current=='corner':
                numColor = (50,50,50)
            cv2.putText(frame, str(edgeCounter+1), (20,105), cv2.FONT_HERSHEY_SIMPLEX ,
                            1, numColor, 2, cv2.LINE_AA)
            
            #current buffer
            points = self.getPoints('edge','U',5) # to find points
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, self.getColor(edgeBuffer[edgeCounter][0]) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('edge','R',1) # to find points
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, self.getColor(edgeBuffer[edgeCounter][1]) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            
            #target
            points = self.getPoints('edge',edgeIndex[edgeCounter][0],int(edgeIndex[edgeCounter][1]))
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, (255,0,255) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('edge',edgeIndex[edgeCounter][2],int(edgeIndex[edgeCounter][3])) 
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, (50,50,50) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            
            
           
            #draw corner sequence
            #counter
            if current=='corner':
                numColor = (80,80,80)
            elif current=='edge':
                numColor = (50,50,50)
            cv2.putText(frame, str(cornerCounter+1), (20,105+240), cv2.FONT_HERSHEY_SIMPLEX ,
                            1, numColor, 2, cv2.LINE_AA)
            
            #current buffer
            points = self.getPoints('corner','L',0) # to find points
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, self.getColor(cornerBuffer[cornerCounter][0]) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('corner','U',0) # to find points
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, self.getColor(cornerBuffer[cornerCounter][1]) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('corner','B',2) # to find points
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, self.getColor(cornerBuffer[cornerCounter][2]) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            
            #target
            points = self.getPoints('corner',cornerIndex[cornerCounter][0],int(cornerIndex[cornerCounter][1]))
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, (255,0,255) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('corner',cornerIndex[cornerCounter][2],int(cornerIndex[cornerCounter][3])) 
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, (50,50,50) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
            points = self.getPoints('corner',cornerIndex[cornerCounter][4],int(cornerIndex[cornerCounter][5])) 
            a1 = np.array( [[[points[0],points[1]],
                             [points[2],points[3]],
                             [points[4],points[5]],
                             [points[6],points[7]]]],
                           dtype=np.int32 )
            cv2.fillPoly( frame, a1, (50,50,50) )
            cv2.polylines(frame, a1 ,True, (50,50,50), 1)
            
      
            cv2.imshow("Result", frame)


            key = cv2.waitKey(1)
            if key == 27: #esc key
                break
            if key == 81: #left arrow key
                if current == 'edge':
                    if (edgeCounter==len(edgeIndex)-1):
                        edgeCounter = 0
                    else:
                        edgeCounter = edgeCounter + 1
                elif current == 'corner':
                    if (cornerCounter==len(cornerIndex)-1):
                        cornerCounter = 0
                    else:
                        cornerCounter = cornerCounter + 1
            if key == 83: #right arrow key
                if current == 'edge':
                    if (edgeCounter==0):
                        edgeCounter = len(edgeIndex)-1
                    else:
                        edgeCounter = edgeCounter - 1
                elif current == 'corner':
                    if (cornerCounter==0):
                        cornerCounter = len(cornerIndex)-1
                    else:
                        cornerCounter = cornerCounter - 1
            if key == 82: #up arrow key
                current = 'edge'
            if key == 84: #down arrow key
                current = 'corner'
    
        self.cap.release()
        cv2.destroyAllWindows()




    def getPoints(self,edgeCorner,face,index):
        '''
        Get the XY points of drawing the cubie face as a polygon 
        
        :param edgeCorner: String input to specify if it from edge or corner sequence
        :param face: the face letter
        :param index: the index of cubie face
        :returns: list
        '''
        if (edgeCorner=='edge'):
            z = 0
        elif (edgeCorner=='corner'):
            z = 1
        
           
        if (face == 'U'):
            #U
            scale1 = 20
            scale2 = 6
            scale3 = -20
            scale4 = 6
            xp = [100,120,140,120]
            yp = [66,72,66,60]
            
        elif (face == 'F'):
            #F
            scale1 = 20
            scale2 = 6
            scale3 = 0
            scale4 = 22
            xp = [60,60,80,80]
            yp = [78,100,106,84]
            
        elif (face == 'R'):
            #R
            scale1 = 20
            scale2 = -6
            scale3 = 0
            scale4 = 22
            xp = [120,120,140,140]
            yp = [96,118,112,90]
            
        elif (face == 'D'):
            #D
            scale1 = 20
            scale2 = 6
            scale3 = 20
            scale4 = -6
            xp = [230,210,230,250]
            yp = [138,144,150,144]
            
        elif (face == 'L'):
            #L
            scale1 = -20
            scale2 = 6
            scale3 = 0
            scale4 = 22
            xp = [270,250,250,270]
            yp = [82,88,66,60]
            
        elif (face == 'B'):
            #L
            scale1 = -20
            scale2 = -6
            scale3 = 0
            scale4 = 22
            xp = [310,330,330,310]
            yp = [94,100,78,72]
            
        
        if (index == 0):
            x = 0
            y = 0
        elif (index == 1):
            x = 0
            y = 1
        elif (index == 2):
            x = 0
            y = 2
        elif (index == 3):
            x = 1
            y = 0
        elif (index == 4):
            x = 1
            y = 1
        elif (index == 5):
            x = 1
            y = 2
        elif (index == 6):
            x = 2
            y = 0
        elif (index == 7):
            x = 2
            y = 1
        elif (index == 8):
            x = 2
            y = 2
        
        scale = 240
        
        #xy points 
        points = [xp[0]+(scale1*y)+(scale3*x),yp[0]+(scale2*y)+(scale4*x)+(scale*z),
                    xp[1]+(scale1*y)+(scale3*x),yp[1]+(scale2*y)+(scale4*x)+(scale*z),
                    xp[2]+(scale1*y)+(scale3*x),yp[2]+(scale2*y)+(scale4*x)+(scale*z),
                    xp[3]+(scale1*y)+(scale3*x),yp[3]+(scale2*y)+(scale4*x)+(scale*z)]
        
        return points
        
        
        
    def getColor(self,face):
        '''
        Get the RGB colors from the face letter
        
        :param face: the face letter
        :returns: RGB color
        '''
        if (face=='U'):
            return ColorDetector.name_to_rgb('white')
        elif (face=='F'):
            return ColorDetector.name_to_rgb('blue')
        elif (face=='R'):
            return ColorDetector.name_to_rgb('orange')
        elif (face=='D'):
            return ColorDetector.name_to_rgb('yellow')
        elif (face=='L'):
            return ColorDetector.name_to_rgb('red')
        elif (face=='B'):
            return ColorDetector.name_to_rgb('green')
                
                
results = Results()
    