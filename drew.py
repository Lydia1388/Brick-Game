# -*- coding: utf-8 -*-
#畫矩形
class Box(object):
    def __init__(self, pygame, canvas, name, rect, color) : #建構式
        self.pygame = pygame
        self.canvas = canvas		#背景
        self.name = name		#物件名稱
        self.rect = rect			#位置&大小
        self.color = color		#顏色
        self.visible = True		#可視True 消除False
    def update(self) :
        if (self.visible) :
            self.pygame.draw.rect(self.canvas, self.color, self.rect)
#畫圓
class Circle(object):
    def __init__(self, pygame, canvas, name, pos, radius, color):
        self.pygame = pygame
        self.canvas = canvas		#背景
        self.name = name		#物件名稱
        self.pos = pos			#位置
        self.color = color		#顏色
        self.radius = radius		#半徑
        self.visible = True		#可視True 消除False

    def update(self):
        if (self.visible):
            self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)
"""
矩形	pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
圓形	pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
橢圓形
pygame.draw.ellipse(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)
直線
pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)

顏色	紀錄RGB  0黑  255白
位置	紀錄座標
線寬	省略不寫為0(實心)
"""
