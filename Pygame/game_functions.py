import  sys
import  pygame
from bullet import Bullet

def chech_keydown_events(event,ai_settings,screen,ship,bullets):
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 向右移动飞船
        # ship.rect.center += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
def fire_bullet(ai_settings,screen ,ship,bullets):
    #如果还没有到达限制，就发着一个子弹
    #创建一颗子弹，并将其加入到编组bullets 中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    #响应按键和鼠标事件
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chech_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chech_keydown_events(event,ship,screen,bullets,ai_settings)

def update_screen(ai_settings,screen,ship,bullets):
    #更新屏幕上的图像，并且切换到新的屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #在飞船和卫星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()


    #让最近绘制的屏幕可见
    pygame.display.flip()