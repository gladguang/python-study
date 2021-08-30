import sys

import pygame

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.inin()
    screen = pygame.display.set_mode((1200,800))
    pygamde.dispaly.set_caption('Alien Invasion')

    
    #  设置背景颜色
    bg_color = (230,230,230)

    #  开始游戏的主循环
    while True:
    
    #监视鼠标键盘事件
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
            #  让最近绘制的屏幕可见
            pygame.display.flip()

