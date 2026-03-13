import pygame
import tkinter as tk
import random,time
import os
import tkinter.font as tkFont

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 506

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Fruit Catcher2.0")

clock = pygame.time.Clock()

font1 = pygame.font.Font('venite.ttf', 35)
font2=pygame.font.Font('knight.otf',36)
font3=pygame.font.Font('egmont.ttf',30)
f3=pygame.font.Font('digi.ttf',34)

basket_width = 125
basket_height = 125
basket = pygame.Rect((SCREEN_WIDTH // 2 - basket_width // 2, 375), (basket_width, basket_height))

# falling_objects = []
# fall_speed = 5
object_size = 65
bomb_size=90

# score = 0
# high_score = 0

# level_time = 60

current_level = 1
target_score_level1 = 50
target_score_level2 = 300

apple =pygame.image.load(r'apple1.png').convert()
pygame.Surface.set_colorkey(apple,WHITE)
apple = pygame.transform.scale(apple, (object_size,object_size))
grape =pygame.image.load(r'grape.jpg').convert()
pygame.Surface.set_colorkey(grape,WHITE)
grape = pygame.transform.scale(grape, (object_size,object_size))
mango =pygame.image.load(r'mango.png').convert()
pygame.Surface.set_colorkey(mango,BLACK)
mango = pygame.transform.scale(mango, (object_size,object_size))
bomb =pygame.image.load(r'bomb.png').convert()
pygame.Surface.set_colorkey(bomb,WHITE)
bomb = pygame.transform.scale(bomb, (bomb_size,bomb_size))
fruits = [apple, grape,mango]
targetfruit=mango

if os.path.exists("high_score.txt"):
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
else:
    high_score = 0
scorehigh=False

def save_high_score(score):
    global high_score,scorehigh
    if score > high_score:
        high_score = score
        scorehigh=True
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))

def create_falling_object():
    obj_type = random.choice(fruits + [bomb])
    x_pos = random.randint(0, SCREEN_WIDTH - object_size)
    return {"type": obj_type, "x": x_pos, "y": -object_size}

def draw_falling_object(obj):
    rect=obj['type'].get_rect()
    rect.center=(obj["x"], obj["y"])
    screen.blit(obj['type'],rect)

def show_score_and_timer(score, time_left,current_level):
    score_text = font2.render(f"Score: ", True, (222, 214, 182))
    score_no=font1.render(f'{score}',True, (222, 214, 182))
    timer_text = font3.render(f"Time Left:      s ", True, (222, 202, 193))
    timer_no = f3.render(f"{time_left}  ", True, (222, 202, 193))
    leveltxt=font2.render(f'LEVEL: {current_level} ',True,(235, 212, 171))
    screen.blit(leveltxt,(100,13))
    screen.blit(score_text, (400 , 13))
    screen.blit(score_no,(500 , 15))
    screen.blit(timer_text, (SCREEN_WIDTH - 200, 15))
    screen.blit(timer_no,(SCREEN_WIDTH - 69, 23))
def draw_floating_scores(floating_scores):
    for floating_score in floating_scores[:]:
        text = font1.render(floating_score["text"], True, floating_score["color"])
        screen.blit(text, (floating_score["x"], floating_score["y"]))
        floating_score["y"] -= 1  # Move the score upward
        floating_score["timer"] -= 1
        if floating_score["timer"] <= 0:
            floating_scores.remove(floating_score)
start=False
def start_tkinter():
    def start_game():
        global start
        start=True
        
        root.destroy()
    
    root = tk.Tk()
    root.title("Fruit Catcher")
    bk=tk.PhotoImage(file='bk1.png')
    lab=tk.Label(root,image=bk)
    lab.place(x=0,y=0)

    tfont=tkFont.Font(family="Courier", size=25, weight="bold")
    tfont2=tkFont.Font(family="Courier", size=20, weight="bold")
    label = tk.Label(root, text="Fruit Catcher", font=tfont,background='#763e23',foreground='#f8e682')
    label.pack(pady=20)

    
    high_score_label = tk.Label(root, text=f"High Score: {high_score}", font=tfont2,background='#763e23',foreground='#d6d3c5')
    high_score_label.pack(pady=10)
    
    start_button = tk.Button(root, text="START", command=start_game, font=("Arial", 22),background='#76341d',foreground='#fbf6d5')
    start_button.pack(pady=20)
    start_button.pack(pady=20)
    root.geometry("300x300")
    
    root.mainloop()
stop=False
def game_loop():
    # global score, current_level, falling_objects, level_time,fall_speed,fruits,bombcount
    global fruits
    running = True
    floating_scores = []
    basket_speed = 8
    falling_objects = []
    fall_speed = 5
    score = 0
    high_score = 0
    level_time = 60
    current_level = 1
    bombcount=0
    time_left = level_time
    bk=pygame.image.load(r'C:\Users\Admin\Pictures\bk.jpeg').convert()
    bk=pygame.transform.scale(bk,(SCREEN_WIDTH, SCREEN_HEIGHT))
    basket_icon =pygame.image.load(r'basket.png').convert()
    pygame.Surface.set_colorkey(basket_icon,BLACK)
    basket_icon = pygame.transform.scale(basket_icon, (basket_height,basket_width))
    screen.blit(bk,(0,0))
    level1_end = font2.render(f"Level 1 Target: 150", True, (222, 214, 182))
    screen.blit(level1_end, (325, SCREEN_HEIGHT // 2-100))
    enterstart = font2.render(f"Click to start", True, (222, 214, 182))
    screen.blit(enterstart, (325, SCREEN_HEIGHT // 2))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    save_high_score(score)
                    pygame.quit()
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            while running:
                screen.blit(bk,(0,0))
                screen.blit(basket_icon,basket)
                rectange=mango.get_rect()
                if current_level==1:
                    rectange.center=(250,40)
                    screen.blit(mango,rectange)       

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        save_high_score(score)
                        pygame.quit()
                        stop = True
                        exit()
            # Handle basket movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and basket.left > 0:
                    basket.move_ip(-basket_speed, 0)
                if keys[pygame.K_RIGHT] and basket.right < SCREEN_WIDTH:
                    basket.move_ip(basket_speed, 0)

                # Generate falling objects
                if random.randint(1, 50) == 1:
                    falling_objects.append(create_falling_object())

                # Update falling objects
                for obj in falling_objects[:]:
                    cur=0
                    obj["y"] += fall_speed
                    if obj["y"] > SCREEN_HEIGHT:
                        falling_objects.remove(obj)
                    
                    elif basket.colliderect(pygame.Rect(obj["x"], obj["y"], object_size, object_size-35)):
                        if obj["type"] == bomb:
                            pygame.mixer.Sound('error.mp3').play()
                            bombcount+=1
                            score -= 5 if current_level == 1 else 10
                            cur='-5' if current_level==1 else '-10'
                            colour=(237, 73, 55)
                        elif current_level == 1 and obj['type']==targetfruit:
                            pygame.mixer.Sound('point1.mp3').play()
                            score += 10
                            cur='+10'
                            colour=(240, 193, 122)
                        else:
                            pygame.mixer.Sound('point1.mp3').play()
                            score+=5
                            cur='+5'
                            colour=(240, 193, 122)
                        floating_scores.append({
                            "text": f"{cur}",
                            "x": obj["x"],
                            "y": obj["y"],
                            "timer": 60,  # Duration the score floats
                            "color": colour
                        })
                        falling_objects.remove(obj)

                for obj in falling_objects:
                    draw_falling_object(obj)

                # Update and display score/timer
                time_left -= 1 / 60
                show_score_and_timer(score, int(time_left),current_level)

                draw_floating_scores(floating_scores)

                # Check for level progression or end game
                if time_left <= 0 or (current_level == 1 and score >= target_score_level1):
                    if current_level == 1:
                        screen.blit(bk,(0,0))
                        current_level += 1
                        time_left = level_time
                        fall_speed+=3
                        bombcount=0
                        fruits=fruits+[bomb,bomb]
                        falling_objects.clear()
                        level1_end = font2.render(f"Level 1 completed", True, (222, 214, 182))
                        screen.blit(level1_end, (325, SCREEN_HEIGHT // 2-100))
                        level2start = font2.render(f"Level 2 Start", True, (222, 214, 182))
                        screen.blit(level2start, (SCREEN_WIDTH // 2 -90, SCREEN_HEIGHT // 2))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        continue
                    elif current_level == 2 and score >= target_score_level2:
                        save_high_score(score)
                        running = False
                if bombcount==3:

                    save_high_score(score)
                    running=False
                    screen.blit(bk,(0,0))
                        
                pygame.display.flip()
                clock.tick(60)

            # End screen
            end_text = font2.render(f"Game Over! Total Score: {score}", True, (222, 214, 182))
            screen.blit(end_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2-50))
            timetaken= font2.render(f'Time Taken: {(level_time-time_left)//1}',True,(222, 214, 182))
            screen.blit(timetaken, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
            high_text = font2.render(f"New High Score", True, (222, 214, 182))
            
            if scorehigh:
                screen.blit(high_text,(SCREEN_WIDTH // 2-100, SCREEN_HEIGHT // 2+50))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(3000)
    

start_tkinter()
if start==True:
    while not stop:
        game_loop()
pygame.quit()
