import pygame 
from pygame.image import load 
from random import randint

#score
def display_score():
   current_time = int(pygame.time.get_ticks()/1000) -start_time#neemt de tijd in ms
   score_surf=font.render(f'{current_time}',False,(46, 222, 213))#argumenten: text, ronderen,kleur
   score_rect= score_surf.get_rect(center = (400,50))
   screen.blit(score_surf,score_rect)
   return current_time


def obstacle_movement(obstacle_list):
   if obstacle_list:
      for obstacle_rect in obstacle_list:
         obstacle_rect.x -=5

         screen.blit(tube_surf,obstacle_rect)
      obstacle_list=[obstacle for obstacle in obstacle_list if obstacle_rect.x > -100]
      return obstacle_list
   else: return []
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    if player.top >= 500 or player.bottom < 0:
        return False
    return True
def player_animation():
   global bird_surf, bird_index
   bird_index+=0.1
   if bird_index >=len(bird_list): 
      bird_index=0
   bird_surf=bird_list[int(bird_index)]
   
   

pygame.init()
#frame rate
clock = pygame.time.Clock()
#screen set up
width = 800
height = 500 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jérôme")
#cPLAYER
bird_walk_1= load('bird game/beelden_bird/player/player_fly_1.png').convert_alpha()
bird_walk_2= load('bird game/beelden_bird/player/player_fly_2.png').convert_alpha()
bird_walk_1=pygame.transform.rotozoom(bird_walk_1,0,2) 
bird_walk_2=pygame.transform.rotozoom(bird_walk_2,0,2) 
bird_list=[bird_walk_1,bird_walk_2]  # Now using bird_walk_1 and bird_walk_2
bird_index=0
bird_surf=bird_list[bird_index]
bird_rect= bird_surf.get_rect(center=(80,200))
player_stand_surf=pygame.transform.rotozoom(bird_surf,0,5) .convert_alpha()
player_stand_rect=player_stand_surf.get_rect(center=(400,200))

bg_Music =pygame.mixer.Sound('first game/audio/music.wav')
bg_Music.play(loops=-1)

#gravity
player_gravity=0
#BACKGROUND
sky_surface= load('bird game/beelden_bird/achtergrond/Sky_6.png').convert_alpha()
sky_surface=pygame.transform.rotozoom(sky_surface, 0, 2.55)
ground_surface= load('bird game/beelden_bird/achtergrond/ground 1.png').convert_alpha()
#obsticals

#tekst


#lettertype
font=pygame.font.Font("bird game/font/Pixeltype.ttf",50)#argumenten lettertype,lettergrootte
#textzelf
#game over
game_over=font.render('GAME OVER',False,(241, 6, 6,))#argumenten: text, ronderen,kleur
game_over_rect=game_over.get_rect(center=(400,50))
instr_surf=font.render('press space to play again',False,(64,64,64))
instr_rect=instr_surf.get_rect(center=(400,400))
#score
score_surf=font.render('score',False,(46, 222, 213))#argumenten: text, ronderen,kleur
score_rect= score_surf.get_rect(center = (400,50))
#score
start_time=0
score=0

#obstacles
obstacle_rect_list=[]
tube_surf=load('bird game/beelden_bird/achtergrond/obstacles.png')
tube_surf2=pygame.transform.rotozoom(tube_surf, 180, 1)
tube_surf=pygame.transform.rotozoom(tube_surf, 0, 2 )
tube_rect=tube_surf.get_rect(center=(600,300))

#timer
obstacle_timer= pygame.USEREVENT +1 

pygame.time.set_timer (obstacle_timer,1600 ) #de 1400 is de tijd tussen de trigger BELANGRIJK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

jump_sound = pygame.mixer.Sound('first game/audio/jump.mp3')
jump_sound.set_volume(0.5)


run = True
game_active=True

while run:
    if game_active:
        #achtergrond
        screen.blit(sky_surface,(0,0)) #afbeelding 'in spawnen' 
        screen.blit(ground_surface,(0,400))#afbeelding grond op het scherm zetten
        #rest
        #obstackle movement
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        player_animation()
        screen.blit(bird_surf,bird_rect)
        score=display_score()
        player_gravity+= 0.45
        bird_rect.y+= player_gravity
        
           
        game_active=collisions(bird_rect,obstacle_rect_list)
      
           
        
        
    else:
       screen.fill((94, 129, 162))
       screen.blit(game_over,game_over_rect)
       screen.blit(instr_surf,instr_rect)
       score_surface=font.render(f'your score is: {score}',False,(64,64,64))
       score_rectangle=score_surface.get_rect(center=(400,100))
       screen.blit(score_surface,score_rectangle)
       bird_rect.y= 100
       player_gravity=0
        
        



    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # om het spel te stoppen
         run = False
         print("quit event detected")
        if game_active:
           if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
              player_gravity=-10
              jump_sound.play()
   
           if event.type== obstacle_timer:
              center_cor1=randint(900,1300) 
              ramdom_cor=randint(75,425)
              bovenste_cor=ramdom_cor-90
              onderste_cor=ramdom_cor+90
              obstacle_rect_list.append(tube_surf.get_rect(bottomright  =(center_cor1,bovenste_cor)))
              obstacle_rect_list.append(tube_surf.get_rect(topright  =(center_cor1,onderste_cor))) 
        else:
           if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
              game_active=  True
              start_time= int(pygame.time.get_ticks() /1000)
              obstacle_rect_list.clear()


    pygame.display.update()
    clock.tick(60)
pygame.quit

#enter_cor1=randint(900,1100) 
 #             ramdom_cor=randint(75,425)
  #            bovenste_cor=ramdom_cor-75
  #            onderste_cor=ramdom_cor+75
  #            obstacle_rect_list.append(tube_surf.get_rect(bottomright  =(center_cor1,bovenste_cor)))
   #           obstacle_rect_list.append(tube_surf.get_rect(bottomright  =(center_cor1,onderste_cor)))