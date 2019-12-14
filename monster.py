# -*- coding -*-
#filename:monster.py
import  pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

#控制怪物动画的速度
COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8

#定义代表怪类型的数量（如果程序需要增加更多怪物，则只需要在此处添加常量即可）
TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3

class monster(Sprite):
    def __init__(self, view_manager, tp = TYPE_BOMB):
        super().__init__()
        #定义怪物的类型
        self.type = tp
        #定义怪物的X,Y坐标属性
        self.x = 0
        self.y = 0
        #定义怪物是否已经死亡的旗标
        self.is_die = False
        #绘制怪物图片左上角的X坐标
        self.start_x = 0
        #绘制怪物图片左上角Y坐标
        self.start_y = 0
        #绘制怪物图片右下角的X坐标
        self.end_x = 0
        #改变量用于控制动画刷新的速度
        self.draw_count = 0
        #定义当前正在绘制怪物动画的第几帧的变量
        self.draw_index = 0
        '''
        用于记录私网的动画只绘制一次，不需要重复绘制
        每当怪物死亡时，改变了都会被初始化为等于死亡动画的总帧数
        当怪物的死亡动画帧播放完成后，该变量的值变为0
        '''
        self.die_max_draw_count = sys.maxsize
        #定义怪物发射的子弹
        self.bullet_list = Group()
        '''
        -------------下面代码根据怪物类型来初始化怪的X，Y坐标-----
        如果怪物是炸弹（TYPE_BOMB）或敌人（TYPE_MAN）
        怪物的Y坐标与玩家控制的角色的Y坐标相同
        '''
        if self.type == TYPE_BOMB or self.type == TYPE_MAN:
            self.y = view_manager.Y_DEFALUT
        #如果怪物是飞机，则根据屏幕高度随机生成怪物的Y坐标
        elif self.type == TYPE_FLY:
            self.y = view_manager.screen_hight * 50 / 100 - randint(0, 99)
        #随机计算怪物的X坐标
        self.x = view_manager.screen_width + randint(0, view_manager.screen_width >> 1) - (view_manager.screen_width >> 2)

    #绘制怪物的方法
    def draw(self, screen, view_manager):
        #如果怪物是炸弹，则绘制炸弹
        if self.type == TYPE_BOMB:
            #死亡的怪物使用死亡的图片时，活着的怪物使用活着的图片
            self.draw_adnim(screen, view_manager, view_manager.bomb2_images
                            if self.is_die else view_manager.bomb_images)
        #如果怪物是人，则绘制人
        elif self.type == TYPE_MAN:
            self.draw_anim(screen, view_manager, view_manager.man_die_images if self.is_die else: view_manager.man_images)
        else:
            pass
    #根据怪物的动画帧图片来绘制怪物动画
    def draw_anim(self, screen, view_manager, bitmap_arr):
        #如果怪物已经死亡，且没有播放死亡动画
        #（self.die_max_draw_count等于初始值， 表明未播放过死亡动画）
        if self.is_die and self.die_max_draw_count == sys.maxsize:
            #将die_max_draw_count设置为与死亡动画的总帧数相等
            self.die_max_draw_count = len(bitmap_arr)
        self.draw_index %= len(bitmap_arr)
        if bitmap = = None:
            return
        draw_x = self.x
        #对绘制怪物动画帧位图的X坐标进行微调
        if self.is_die:
            if type == TYPE_BOMB:
                draw_x = self.x - 50
            elif type == TYPE_MAN:
                draw_x = self.x + 50
        #对绘制怪物的动画位的Y坐标进行微调
        draw_y = self.y - bitmap.get_height()
        #绘制怪物动画帧的位图
        screen.blit(bitmap, (draw_y, draw_y))
        self.start_x = draw_x
        self.start_y = draw_y
        self.end_x = self.start_x + bitmap.get_width()
        self.end_y = self.start_y + bitmap.get_height()
        self.draw_count += 1
        #控制人、费劲发射子弹的速度
        if self.draw_count > = (COMMON_SPEED_THRESHOLD if type == TYPE_MAN else MAN_SPEED_THRESHOLD):
            #如果怪物是人，则只在第3帧才发子弹
            if self.type == TYPE_MAN and self.draw_index ==2:
                self.add_bullet()
        




