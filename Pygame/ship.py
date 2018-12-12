import  pygame

class Ship():

    def __init__(self,screen):
        # 初始化飞船并设置其初始值
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rent = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.center = self.screen_rent.centerx
        self.rect.bottom = self.screen_rent.bottom

    def biltme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
