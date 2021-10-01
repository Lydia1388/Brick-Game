# -*- coding: utf-8 -*-
#引入模組
import random, pygame
from drew import *

# 視窗大小(寬*高)
canvas_width = 800
canvas_height = 600

# 背景顏色RGB
block = (50,50,50)

# 磚塊串列
bricks_list = [ ]

# 定義變數
game_mode = 0	# 遊戲狀態 : 0靜止 / 1遊戲進行中
dx = 10			# 球 x方向(水平)移動速度
dy = -10			# 球 y方向(垂直)移動速度

#定義函式 : 顯示文字
def showFont(text, x, y):
    global canvas
    font = pygame.font.SysFont("simhei", 30)
    text = font.render(text, 1, (255, 100, 0))
    canvas.blit( text, (x, y))
    #				x(右)y(下)
#定義函式 : 碰撞判斷
def  isCollision(x, y, boxRect) :
    if (x >= boxRect[0] and x <= boxRect[0] + boxRect[2] and
         y >= boxRect[1] and y <= boxRect[1] + boxRect[3]) :
            return True
    return False
#定義函式 : 初始化遊戲
def resetGame():
    global game_mode, brick_num, bricks_list, dx, dy
    # 磚塊
    for bricks in bricks_list :
        # 亂數磚塊顏色
        r = random.randint(200, 255)
        g = random.randint(0, 10)
        b = random.randint(100, 255)
        bricks.color = [r, g, b]
        # 開啟磚塊
        bricks.visible = True

    game_mode = 0  # 遊戲狀態
    brick_num = 121  # 磚塊數量
    dx = 10  # 水平移動速度
    dy = -10  # 垂直移動速度

# 初始化函式 一定要有!!!
pygame.init()
# 視窗Title
pygame.display.set_caption("Brick Game")
# 建立畫布大小 800*600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
# 時脈物件
clock = pygame.time.Clock( )
"""
PyGame中的時間以毫秒為單位。
pygame.time.get_ticks()		獲取以毫秒爲單位的時間
pygame.time.wait()			暫停程式一段時間
pygame.time.delay()			暫停程式一段時間
pygame.time.set_timer() 		在事件隊列上重複創建一個事件
pygame.time.Clock()			創建一個物件來幫助追蹤時間
"""
# 反彈板板
paddle_x = 0
paddle_y = (canvas_height - 50)	#差值越小板板越高
paddle = Box(pygame, canvas, "paddle", [paddle_x, paddle_y, 100, 24], (255,255,255))

# 球
ball_x = paddle_x
ball_y = paddle_y
ball = Circle(pygame, canvas, "ball", [ball_x, ball_x], 8, (255,255,255))
# 建立磚塊
brick_num = 0
brick_x = 70
brick_y = 60
brick_w = 0
brick_h = 0
for i in range( 0, 121):
    if((i % 11)==0):
        brick_w = 0
        brick_h = brick_h + 18	#上下間距2
    bricks_list.append (Box(pygame, canvas, "brick_"+str(i),
                        [brick_w+brick_x, brick_h+brick_y, 58, 16], [255, 255, 255]))
    brick_w = brick_w + 60		#左右間距2
# 呼叫函式 : 初始化遊戲
resetGame()
# 主迴圈開始
running = True
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : # 離開遊戲
            running = False
        if event.type == pygame.KEYDOWN : # 鍵盤
            if event.key == pygame.K_ESCAPE : # ESC鍵
                running = False
    if event.type == pygame.MOUSEMOTION : # 判斷Mouse
        paddle_x = pygame.mouse.get_pos()[0] - 50
    if event.type == pygame.MOUSEBUTTONDOWN :
        if game_mode == 0 : # 遊戲狀態 : 0靜止 / 1遊戲進行中
            game_mode = 1

    canvas.fill(block) # 清除畫面，不然畫面上會留一堆殘影

    for bricks in bricks_list:  # 磚塊感測
        if isCollision(ball.pos[0], ball.pos[1], bricks.rect):  # 球碰磚塊
            if bricks.visible:
                brick_num = brick_num - 1  # 扣除磚塊
                if brick_num == 0:  # 磚塊沒了
                    resetGame()  # 重開一局，初始化遊戲
                    break
                dy = -dy  # 球反彈
            bricks.visible = False  # 關閉磚塊
        bricks.update()  # 更新磚塊

    showFont("bricks:" + str(brick_num), 50, 40)  # 顯示剩餘磚塊數 座標參數(右, 下)

    paddle.rect[0] = paddle_x  # 讓板板跟著滑鼠動
    paddle.update()  # 顯示板板

    if isCollision(ball.pos[0], ball.pos[1], paddle.rect):  # 球碰板板
        dy = -dy

    # 遊戲狀態 : 0靜止 / 1遊戲進行中

    if game_mode == 0:  # 等開球
        ball.pos[0] = ball_x = paddle.rect[0] + ((paddle.rect[2] - ball.radius) >> 1)
        ball.pos[1] = ball_y = paddle.rect[1] - ball.radius

    elif game_mode == 1:  # 開球
        ball_x += dx
        ball_y += dy
        if ball_y + dy > canvas_height - ball.radius:
            game_mode = 0  # 死亡
        if ball_x + dx > canvas_width - ball.radius or ball_x + dx < ball.radius:
            dx = -dx  # 左右邊界碰撞
        if ball_y + dy > canvas_height - ball.radius or ball_y + dy < ball.radius:
            dy = -dy  # 上下邊界碰撞
        ball.pos[0] = ball_x
        ball.pos[1] = ball_y
    ball.update()  # 更新球球
    # 更新畫面
    pygame.display.update()
    clock.tick(60)
# 主迴圈結束

pygame.quit()  # 離開遊戲
"""
pygame.time.Clock()  
pygame.time.Clock.tick()					更新時鐘
pygame.time.Clock.tick_busy_loop()		更新時鐘
pygame.time.Clock.get_time()			在上一個tick中使用的時間
pygame.time.Clock.get_rawtime()			在上一個tick中使用的實際時間
pygame.time.Clock.get_fps()				計算時鐘幀率
"""
