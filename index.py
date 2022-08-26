import random
import pygame
import sys
import time

change = True
sleep_time = 0.15

#세팅
rooms = [0,0,0]
room_index = [0,1,2]
left_room_index = [0,1,2]
key_room_index = random.randint(0,2)
rooms[key_room_index] = 1
choose = random.randint(0,2)

success_count = {"성공": 0, "실패": 0}

pygame.init()

#화면 크기 설정
screen_width = 640 #가로 크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(color=(255,255,255))

pygame.display.set_caption("monty hall")

def select_one_first():
    
    global rect1_type
    global rect2_type
    global rect3_type
    global rect1_color
    global rect2_color
    global rect3_color
    global human_position
    global rooms
    global room_index
    global left_room_index
    global key_room_index
    global choose
    
    #세팅
    rooms = [0,0,0]
    room_index = [0,1,2]
    left_room_index = [0,1,2]

    key_room_index = random.randint(0,2)
    rooms[key_room_index] = 1

    choose = random.randint(0,2)


    #선택은 푸른색으로 보여주기
    if(choose == 0):
        human_position = (160-5, 200)
        rect1_color = (0, 100, 255)
    elif(choose == 1):
        human_position = (320-5, 200)
        rect2_color = (0, 100, 255)
    elif(choose == 2):
        human_position = (480-5, 200)
        rect3_color = (0, 100, 255)
    else:
        print("error")
        exit()
    
def show_empty_room():
    global rect1_type
    global rect2_type
    global rect3_type
    global rect1_color
    global rect2_color
    global rect3_color
    global human_position
    global rooms
    global room_index
    global left_room_index
    global key_room_index
    global choose
    
    #선택후 보여줘야 하는 index 구하기
    room_index.remove(key_room_index)

    if(rooms[choose] == 0):
        room_index.remove(choose)
    elif(rooms[choose] == 1):
        
        show_room_index = random.choice(room_index)
        
        room_index.remove(show_room_index)
    else:
        print("error")
        exit()
        
    #보여주는 방 투명화
    if(room_index[0] == 0):
        rect1_type = 1
    elif(room_index[0] == 1):
        rect2_type = 1
    elif(room_index[0] == 2):
        rect3_type = 1
    
    #보여주기 남은 2개의 index
    left_room_index.remove(room_index[0])
def change_room():
    global rect1_type
    global rect2_type
    global rect3_type
    global rect1_color
    global rect2_color
    global rect3_color
    global human_position
    global rooms
    global room_index
    global left_room_index
    global key_room_index
    global choose
    
    #change = random.choice([True, False])
    
    #바꾸기 여부
    result_room_index = None
    if(change):
        left_room_index.remove(choose)
        result_room_index = left_room_index[0]
    else:
        result_room_index = choose
    
    #2차 바꾸기 후 선택: 주황색
    if(result_room_index == 0):
        human_position = (160-5, 200)
        rect1_color = (255, 100, 0)
    elif(result_room_index == 1):
        human_position = (320-5, 200)
        rect2_color = (255, 100, 0)
    elif(result_room_index == 2):
        human_position = (480-5, 200)
        rect3_color = (255, 100, 0)
        
    
    #성공 판단
    is_success = "성공" if rooms[result_room_index] == 1 else "실패"
    
    success_count[is_success] += 1
    
    return is_success

def show_key():
    global key_room_index
    global screen
    
    #key 보여주기
    if(key_room_index == 0):
        pygame.draw.circle(screen, (255,255,0), (160, 70), 10)
    elif(key_room_index == 1):
        pygame.draw.circle(screen, (255,255,0), (320, 70), 10)
    elif(key_room_index == 2):
        pygame.draw.circle(screen, (255,255,0), (480, 70), 10)

def draw_screen():
    global screen
    global rect1_type
    global rect2_type
    global rect3_type
    global rect1_color
    global rect2_color
    global rect3_color
    global human_position
    
    screen.fill(color=(255,255,255))
         
    pygame.draw.rect(screen,rect1_color,(160-50,20,100,100), rect1_type)        
    pygame.draw.rect(screen,rect2_color,(320-50,20,100,100), rect2_type)
    pygame.draw.rect(screen,rect3_color,(480-50,20,100,100), rect3_type)
    
    pygame.draw.circle(screen,(100,100,255),human_position,20)

running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중

rect1_type = 0
rect2_type = 0
rect3_type = 0
rect1_color = (0,0,0)
rect2_color = (0,0,0)
rect3_color = (0,0,0)


human_position = (320,380)

count = 0

while running:
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False
        
    count += 1
    
    rect1_color = (0,0,0)
    rect2_color = (0,0,0)
    rect3_color = (0,0,0)
    rect1_type = 0
    rect2_type = 0
    rect3_type = 0
    
    #=========
    select_one_first()
    draw_screen()
    pygame.display.update() 
    pygame.time.delay(int(sleep_time * 1000))
    
    #=========
    
    show_empty_room()
    draw_screen()
    pygame.display.update() 
    pygame.time.delay(int(sleep_time * 1000))
    
    #=========
    
    change_room()
    draw_screen()
    show_key()
    pygame.display.update() 
    pygame.time.delay(int(sleep_time * 1000))
    #=========
    
    rect1_color = (0,0,0)
    rect2_color = (0,0,0)
    rect3_color = (0,0,0)
    rect1_type = 0
    rect2_type = 0
    rect3_type = 0
    human_position = (320,380)
    
    draw_screen()
    pygame.display.update() 
    pygame.time.delay(int(sleep_time * 1000))
        
    
    print(success_count)
    print(f"count : {count}")
    
print(f"성공률 : {success_count['성공'] / (success_count['성공'] + success_count['실패']) * 100}%")
sys.exit()