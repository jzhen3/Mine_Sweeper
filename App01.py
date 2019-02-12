#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:36:35 2017

@author: jinsongzhen
"""
from tkinter import *
import random

class TestApp(object):
    def __init__(self,x,y):
        self.root= Tk()
     
        self.height= y
        self.width = x
        self.board = self.create_board(self.width,self.height)
        self.bury_mines(7)
                
    def draw_lost_board(self):
   
        for i in range(self.height):                                                              
            for j in range(self.width):    
                if self.board [i][j] == -1:                      
                    self.c.create_rectangle(i*100,j*100,1000,1000, fill = "red")
                    
                else: 
                    self.c.create_rectangle(i*100,j*100,1000,1000, fill = "light green")     
                    self.c.create_text(i*100+50,j*100+50,font =100, text= self.get_mine_count(i,j)) 
                
                    
    def draw_board(self):
        for i in range(self.height):                                                              
            for j in range(self.width):    
                if self.board [i][j] == -1:                      
                    self.c.create_rectangle(i*100,j*100,1000,1000, fill = "light green")
                elif self.board[i][j] == None:
                    self.c.create_rectangle(i*100,j*100,1000,1000, fill = "light green")   
                else: 
                    self.c.create_rectangle(i*100,j*100,1000,1000, fill = "light blue")   
                    self.c.create_text(i*100+50,j*100+50, text= self.get_mine_count(i,j)) 
                
             
    def run(self):
        lose = None
        self.c = Canvas(master =self.root, height=self.height*100, width =self.width*100)     
        self.c.pack() 
        
        self.c.bind("<Button-1>",self.handle_click)
        
        self.draw_board()
        if lose == -1:
            print ('you lose')
        if self.check_won (self.board) == True:
            print ('you win')
            
        
        
        self.root.mainloop()
        
        
             
        #while True:
        #    x = int(input ("please give me x value"))
        #    y = int(input ("please give me y value"))
        # 
        #    if self.board[x][y] == -1:
        #        print (False)
        #        break
        # 
        #    else:
        #        uncover_board(self.board,x,y)
        #        user_view(self.board)
        #        if check_won(self.board) == True:
        #            print ('you have won the game')
        #            break
  
    def handle_click(self, event):

        row = event.y // 100
        column = event.x // 100 
        print(row, column)
        self.uncover_board(column, row)
        self.draw_board()
        
    
        
    def create_board(self, width, height):
        self.board = []
        for i in range(height):
            list1 = []
            self.board.append(list1)
            for j in range(width):
                list1.append(None)        
                
        return self.board
        
    def bury_mines(self,mine_amount):
        mine_counter = 0
        while mine_counter != mine_amount:
            i = random.randint(0,self.height- 1)
            j = random.randint(0,self.width- 1)    
            if self.board[i][j] == None:
                self.board[i][j] = -1
                mine_counter += 1
        return (self.board)
    
    def get_mine_count(self,x,y):
        counter=0
        distance=[-1,0,1]
        height=len(self.board)
        width=len(self.board[0])
        for i in distance:
            for j in distance:
                if x+i>=0 and y+j>=0 and x+i<height and y+j<width:
                    if x+i!=x or y+j!=y:
                        if self.board[x+i][y+j]== -1:
                            counter+=1
        return counter        
        
    def uncover_board(self, x, y):
        
        gameboard = self.board
        if gameboard[x][y]== -1:
            lose = -1
        if gameboard[x][y] !=None:
            return 
        elif self.get_mine_count(x,y) > 0:
            gameboard[x][y] = self.get_mine_count(x, y)
        
        elif self.get_mine_count(x,y) == 0:
            gameboard[x][y] = 0
            distance=[-1,0,1]
            for i in distance:
                for j in distance:
                    if x+i>=0 and y+j>=0 and x+i<self.height and y+j<self.width: # coordinate on board
                        if x+i!=x or y+j!=y:   # coordinate not the same as x and y    
                            self.uncover_board(x+i, y+j)
                             
    
    def check_won(self, board):
        for i in range (len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == None:
                    return False          
                    
        return True
        print ("you win!", self.board[i][j])
        
app = TestApp(7,7)
app.run()     


'''
    def game(self, height, width, mine_amount):
        for i in range(len(height)):
            for j in range(len(width)):
                height = 100
                width =  100
                mine_amount =input("give me the number of mines", n)
'''
