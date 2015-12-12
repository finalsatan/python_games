# -*- coding: utf-8 -*-


__author__ = 'finalsatan'


"""
A simple 2048 game
"""

import random
import sys
import os


class game2048(object):
	
	n = 0 #维度
	nlist = [] #矩阵
	numlist = [2,2,2,4] #取值数组
	start_flag = 0 #游戏开始标志
	end_flag = 0 #游戏结束标志
	move_flag = 0 #移动是否有效标志

	#2048 初始化函数
	def __init__(self, n):
		self.n = n
		self.nlist = list( list( 0 for i in range(n) ) for i in range(n) )

		#########<随机两个位置为2或4>#############		
		x_first = random.randint(0,self.n-1)
		y_first = random.randint(0,self.n-1)
		self.nlist[x_first][y_first] = random.choice(self.numlist)

		x_second = random.randint(0,self.n-1)
		y_second = random.randint(0,self.n-1)

		while ( (x_second == x_first) & (y_second == y_first) ):
			x_second = random.randint(0,self.n-1)
			y_second = random.randint(0,self.n-1)

		self.nlist[x_second][y_second] = random.choice(self.numlist)
		#########</随机两个位置为2或4>#############


	def nlistModify(self,action):
		#根据用户输入的上i、下k、左j、右l,图形进行相应的变化
		originalMatrix = [] #保存原始矩阵，用于判断矩阵是否发生了变化
		for i in range(self.n): #初始化原始矩阵
			originalMatrix.append([])
			for j in range(self.n):
				#self.nlist[i][j] = 0
				originalMatrix[i].append(self.nlist[i][j])
		#print "originalMatrix1:",originalMatrix
		#self.outPut(originalMatrix)

		nlistModify = []
		nlistModifyBack = []
		self.move_flag = 0 #用于判定本次用户输入方向的移动是否有效

		if( action == 'i' ):#矩阵向上移动
			for i in range(self.n):
				#print self.n,i
				nlistModify.append([row[i] for row in self.nlist])#将矩阵的列变成行
			#print "nlistModify_matrix:"
			#self.outPut(nlistModify)
			nlistModify = self.matrixMove(nlistModify)#矩阵向左移动
			#print "nlistModify_matrix_move:"
			#self.outPut(nlistModify)
			for i in range(self.n):
				#print self.n,i
				nlistModifyBack.append([row[i] for row in nlistModify])#将矩阵的列变成行
			self.nlist = nlistModifyBack
		elif( action == 'j' ):#矩阵向左移动
			self.nlist = self.matrixMove(self.nlist)
			#print "nlistModify_self.nlist:",self.nlist
		elif( action == 'k' ):#矩阵向下移动
			for i in range(self.n):
				#print self.n,i
				nlistModify.append([row[i] for row in self.nlist])#将矩阵的列变成行
			for i in range(self.n):
				nlistModify[i].reverse()#将矩阵的顺序左右颠倒
			nlistModify = self.matrixMove(nlistModify)#矩阵向左移动
			for i in range(self.n):
				nlistModify[i].reverse()#将矩阵的顺序左右颠倒
			for i in range(self.n):
				#print self.n,i
				nlistModifyBack.append([row[i] for row in nlistModify])#将矩阵的列变成行
			self.nlist = nlistModifyBack
		elif( action == 'l' ):#矩阵向右移动
			nlistModify = self.nlist
			for i in range(self.n):
				nlistModify[i].reverse()#将矩阵的顺序左右颠倒
			nlistModify = self.matrixMove(nlistModify)#矩阵向左移动
			nlistModifyBack = nlistModify
			for i in range(self.n):
				nlistModifyBack[i].reverse()#将矩阵的顺序左右颠倒
			self.nlist = nlistModifyBack
		else:
			pass
		#print "originalMatrix2:"
		#self.outPut(originalMatrix)
		#print "movedMatrix:"
		#self.outPut(self.nlist)

		for i in range(self.n):
			for j in range(self.n):
				if ( originalMatrix[i][j] != self.nlist[i][j] ):
					self.move_flag = 1
					break
			if (self.move_flag):
				break



	def matrixMove(self,matrix):#矩阵从右向左移动，相同的数字合并，空余位置补0
		m = matrix
		#print "matrix:",matrix
		length = len(matrix)
		for i in range(length):
			m[i] = self.listMove(m[i])
			#print "m[i]:",m[i]
		return m
		#print "matrixMove_self.nlist:",self.nlist


	def listMoveOnce(self,single_list):#每次合并一个数字
		l = single_list
		len_list = len(single_list)#列表的长度
		#print "list:"
		#print l
		#print "listlength:"
		#print len_list
		flag = 0
		zero_flag = 0


		for i in range(len_list-1):
			if  (l[i] == 0):
				zero_flag = zero_flag + 1
				continue
			else:
				j = i + 1
				if (j<len_list):
					while (l[j] == 0):
						j = j + 1
						if j > len_list -1 :
							break
						#print "j:",j
						#print "len_list:",len_list
						pass
					if (j<len_list):
						if (l[i] == l[j]):
							l[i] = l[i] + l[j]
							t_i = i + 1
							t_j = j + 1
							while (t_i < len_list)&(t_j < len_list):
								l[t_i] = l[t_j]
								t_i = t_i + 1
								t_j = t_j + 1
							while (t_i < len_list):
								l[t_i] = 0
								t_i = t_i + 1

							flag = flag + 1
				break
		#print "l:",l
		#print "j:",j
		#print "zero_flag:",zero_flag
		#print "zero_flag:",zero_flag
		for k in range(len_list-zero_flag):
			l[k] = l[k+zero_flag]
		for t_k in range(zero_flag):
			#print "k:",k
			#print len_list-1-k
			l[len_list-1-t_k] = 0
		if flag == 0:
			flag = 1
		return flag , l


	def listMove(self,single_list):#列表从后向前移动,相同的数字合并，空余位置补0
		p = 0
		len_list = len(single_list)#列表的长度
		p,l = self.listMoveOnce(single_list)
		while (p < len_list):
			#print "p:"
			#print p
			q,l[p:] = self.listMoveOnce(single_list[p:])
			#print "q:"
			#print q
			if(	q==0 ):
				break
			p = p + q
		return l


	def randomNum(self, n=1):
		#根据用户输入，图形进行相应的变化后，剩余为0的位置随机出现2或4
		zero_list = []
	
		for i in range(self.n):
			for j in range(self.n):
				if self.nlist[i][j] == 0:
					zero_list.append([i,j])

		random_ij = random.sample(zero_list, n)
		for ij in random_ij:
			self.nlist[ij[0]][ij[1]] = random.choice(self.numlist)


	def isEnd(self):
		#判断游戏是否结束
		originalMatrix = self.nlist #保存原始矩阵，用于判断完成后，恢复原始矩阵
		self.end_flag = 1
		for i in range(self.n):
			for j in range(self.n):
				if (self.nlist[i][j] == 0):
					self.end_flag = 0
					break
			if (self.end_flag == 0) :
				break
		for m in ['i','j','k','l']:
			self.nlistModify(m)
			if self.move_flag == 1:
				self.end_flag = 0
				break
		self.nlist = originalMatrix


	
	def outPut(self,matrix):
		'''
		Output the 2048 matrix
		'''
		for single_list in matrix:
			print(single_list)
		print ("                                      ")


if __name__=="__main__":

    print("\nPlease input j,k,l,i to move.\nj:left\nl:right\ni:up\nk:down\n")

    game = game2048(4)

    while not game.isEnd():
        game.outPut(game.nlist)
        m = input("Please move:")
        game.nlistModify(m)
        if (game.move_flag):
            game.randomNum()
    
    print("GameOver!!!")
    