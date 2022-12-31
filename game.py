import pygame, sys
from pygame.locals import *
import time

pygame.init()

d = pygame.display.set_mode((800, 700))
background = pygame.image.load('pic.png')
background = pygame.transform.scale(background,(800,700))
icon = pygame.image.load("pic1.png")

pygame.display.set_caption('FOLDING BLOCKS')
pygame.display.set_icon(icon)

WHITE = (255, 255, 255) 
BLACK = (0,0,0)
BRIGHT_GREEN = (0, 200, 0)
DARK_GREEN =(102,204,0)
DARK_ORANGE = (204,102,0)
CREAM = (255,255,204)
GREY=(153,153,153)
ORANGE_RED = (255,102,51)
GRAY = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
RED= (255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255, 128,0)
PURPLE=(255,0,255)
CYAN=(0, 255, 255)
bgcolor=(77,71,71)
blue=(0,162,255)
orange=(255,153,0)
purple=(210,36,210)
green=(43,255,0)
red=(255,0,51)
yellow=(255,230,0)
grey=(77,71,71)
DIM_GREY = (105,105,105)
pink=(255,51,53)
bg=(204,255,255)

FPS = 20 # frames per second setting  
fpsClock = pygame.time.Clock() 

em=grey
bg4=WHITE
col0=blue
col1=orange
col2=purple
col3=green
col4=red
col5=yellow
catx=0
cat1y=0
caty=580
cat1x=650
catImg = pygame.image.load('cat3.png') 

rows=0
columns=0
nreq=[]
color=[]
colore=[]
grid=[]
undo=[]
done=False
n=0 #n stores number of clours used in the game

sound0bj = pygame.mixer.music.load('HappyLife.mp3')
pygame.mixer.music.play(-1,0.0)


def w1():
    fontObj = pygame.font.SysFont("freesansbold.ttf",60)
    fontObj1 = pygame.font.SysFont("freesansbold.ttf",90)
    fontObj2 = pygame.font.SysFont("freesansbold.ttf",70)
    
    textSurfaceObj = fontObj1.render('FOLDING', True, GREY)
    textSurfaceObj1 = fontObj2.render('BLOCKS', True, ORANGE_RED)
    textSurfaceObj2 = fontObj.render('PLAY', True, DARK_ORANGE)
    textSurfaceObj3 = fontObj.render('LEVELS', True, DARK_GREEN)
    textSurfaceObj4 = fontObj.render('EXIT', True, ORANGE_RED)
    
    def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
    
    
    setting = pygame.image.load('settings.png')
    
   
    
        
    while True: 
        
        for event in pygame.event.get():
           if event.type == QUIT:
                pygame.quit()
                sys.exit()
           
           mouse=pygame.mouse.get_pos()
           click=pygame.mouse.get_pressed()
           if 340<mouse[0]<440 and 340<mouse[1]<380:
                textSurfaceObj2 = fontObj.render('PLAY', True, ORANGE)
                if click[0]==1:
                    w4(1)
           else:
                textSurfaceObj2 = fontObj.render('PLAY', True, DARK_ORANGE)
                
    
           if 320<mouse[0]<480 and 390<mouse[1]<430:
                textSurfaceObj3 = fontObj.render('LEVELS', True, DARK_GREEN)
    
                if click[0]==1:
                    w3()
                    
           else:
                textSurfaceObj3 = fontObj.render('LEVELS', True, BRIGHT_GREEN)
    
    
           if 340<mouse[0]<430 and 440<mouse[1]<480:
                textSurfaceObj4 = fontObj.render('EXIT', True, ORANGE_RED)
                if click[0]==1:
                    pygame.quit()
                    sys.exit()
    
           else:
                textSurfaceObj4 = fontObj.render('EXIT', True, DARK_ORANGE)
    
    
           if click[0]==1 :
                if 695<mouse[0]<750 and 35<mouse[1]<90:
                    w2()

        d.fill(WHITE)
        blit_alpha(d,background,(0,0),128)
        d.blit(textSurfaceObj, (270,180))
        d.blit(textSurfaceObj1, (300,250))
        d.blit(textSurfaceObj2, (340,340))
        d.blit(textSurfaceObj3, (320,390))
        d.blit(textSurfaceObj4, (340,440))
        d.blit(setting,(700,40))
    
        pygame.display.update()
 
       
def w2():
    fontObj = pygame.font.SysFont('freesansbold.ttf',50)
    fontObj1 = pygame.font.Font('freesansbold.ttf',30)
    fontObj2 = pygame.font.SysFont('freesansbold.ttf',25)
    
    textSurfaceObj1 = fontObj.render('Sound:', True, ORANGE_RED)
    textSurfaceObj2 = fontObj.render('How to Play:', True, DIM_GREY)
    
    surfaceObj = fontObj1.render('ON',True,BLACK,GREY)
    textObj = surfaceObj.get_rect()
    textObj.center = (200,220)
    
    surfaceObj1 = fontObj1.render('OFF',True,BLACK,GREY)
    textObj1 = surfaceObj1.get_rect()
    textObj1.center = (200,290)
    
    
    def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
    
    
    
    s=["Instructions: ","1. It's all about Duplicating certain squares.",
       "2. Focus on symmetry, then the game will be right up your street.",
       "3. Flip the tiles right, left, up, down to completely fill the grid.",
       "4. Use UNDO button to undo your last move.",
       "5. Use REPLAY button to replay the level.",
       "6. Select the level of your choice and have fun playing!"]
    
    
    back = pygame.image.load('reply-all-button.png')
    sound = pygame.image.load('speaker.png')
    sound1 = pygame.image.load('no-sound.png')
    
    
    
    # def main()
        
    while True: # main game loop
        
       
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
            if 170<mouse[0]<230 and 200<mouse[1]<240:
                surfaceObj = fontObj1.render('ON',True,WHITE,GREY)
                textObj = surfaceObj.get_rect()
                textObj.center = (200,220)
                if click[0]==1:
                    pygame.mixer.music.unpause()
            else:
                surfaceObj = fontObj1.render('ON',True,BLACK,GREY)
                textObj = surfaceObj.get_rect()
                textObj.center = (200,220)
            
            if 160<mouse[0]<240 and 270<mouse[1]<310:
                surfaceObj1 = fontObj1.render('OFF',True,WHITE,GREY)
                textObj1 = surfaceObj1.get_rect()
                textObj1.center = (200,290)
                if click[0]==1:
                    pygame.mixer.music.pause()
                    # pass
            else:
                surfaceObj1 = fontObj1.render('OFF',True,BLACK,GREY)
                textObj1 = surfaceObj1.get_rect()
                textObj1.center = (200,290)
    
            if click[0]==1 and (35<mouse[0]<90 and 30<mouse[1]<80):
                return
          
    
        d.fill(WHITE)
        blit_alpha(d,background,(0,0),128)
     
        d.blit(textSurfaceObj1, (90,150))
        d.blit(textSurfaceObj2, (90,380))
    
        d.blit(surfaceObj, textObj)    
        d.blit(surfaceObj1, textObj1)
    
        for i in range(7):
            pygame.draw.rect(d,GREY,(150,430+34*i,600,50))
            d.blit((fontObj2.render(s[i], True, BLACK)), (190,450+26*i))
    
        d.blit(sound, (350,185))
        d.blit(sound1, (350,260))
        
        d.blit(back, (30,30)) 
    
        pygame.display.update()

def w3():
    def main():
        global d
        global done
        d = pygame.display.set_mode((800,700))
        pygame.display.set_caption('LEVELS !')
        d.fill((204,255,255))
        
        back = pygame.image.load('reply-all-button.png')
        
        while not done:
            font = pygame.font.SysFont('Arial', 25)
        
            #drawboard()
            fontObj = pygame.font.Font("freesansbold.ttf",50)
            textSurfaceObj = fontObj.render('LEVELS', True, BLACK, bg)
            textRectObj = textSurfaceObj.get_rect() 
            textRectObj.center = (400,50)
            
            fontObj1 = pygame.font.Font("freesansbold.ttf",32)
            textSurfaceObj1 = fontObj1.render('EASY', True, BLACK, bg)
            textRectObj1 = textSurfaceObj.get_rect() 
            textRectObj1.center = (420,150)
            
            for i in range(5):
                pygame.draw.rect(d,pink,(250+i*75,180,45,45))
                d.blit(font.render(str(i+1), True, (0,0,0)), (255+i*75,180))

                
            fontObj2 = pygame.font.Font("freesansbold.ttf",32)
            textSurfaceObj2 = fontObj2.render('MIDDLE', True, BLACK, bg)
            textRectObj2 = textSurfaceObj.get_rect() 
            textRectObj2.center = (420,320)
            
            for i in range(5):
                pygame.draw.rect(d,blue,(250+i*75,350,45,45))
                d.blit(font.render(str(i+6), True, (0,0,0)), (255+i*75,350))

            
            fontObj3 = pygame.font.Font("freesansbold.ttf",32)
            textSurfaceObj3 = fontObj3.render('HARD', True, BLACK, bg)
            textRectObj3 = textSurfaceObj3.get_rect() 
            textRectObj3.center = (380,500)
            
            for i in range(5):
                pygame.draw.rect(d,green,(250+i*75,530,45,45))
                d.blit(font.render(str(i+11), True, (0,0,0)), (255+i*75,530))

            
            for event in pygame.event.get():
                 
                   if event.type == QUIT:
                       '''pygame.quit()
                       sys.exit()'''
                       done=True
                   mouse=pygame.mouse.get_pos()
                   click=pygame.mouse.get_pressed()
               
                   
                         
                   if click[0]==1 and (30<mouse[0]<90 and 30<mouse[1]<80):
                       w1()
                   if click[0]==1:
                       l=getLevelAtPixel(mouse[0],mouse[1])
                       w4(l)
              
            d.blit(textSurfaceObj, textRectObj)
            del fontObj
            d.blit(textSurfaceObj1, textRectObj1)
            del fontObj1
            d.blit(textSurfaceObj2, textRectObj2)
            del fontObj2
            d.blit(textSurfaceObj3, textRectObj3)
            del fontObj3
            d.blit(back, (30,30)) 
            pygame.display.update()
      
    def getLevelAtPixel(x, y):
         for i in range(5):
             if y>180 and y<180+45 and x>250+75*i and x<295+75*i:
                 return i+1
             elif y>350 and y<350+45 and x>250+75*i and x<295+75*i:
                 return 5+i+1
             elif y>530 and y<530+45 and x>250+75*i and x<295+75*i:
                 return 10+i+1

             
    if _name_ == '_main_':
        main()
        
    pygame.quit()
    
def w4(level):
    def main(level):
        global color
        global colore
        global grid
        global undo
        global d
        global done
        global rows
        global columns
        global nreq
        global catx,cat1y
        
        pygame.init()
        
        d = pygame.display.set_mode((800,700))
        pygame.display.set_caption('Hello World !')
        
        #global level
        #14,15 
        makegrid(level)
        d.fill(WHITE)
        
        
                    
        while not done:
            
          
            
           fontObj = pygame.font.Font("freesansbold.ttf",32)
           textSurfaceObj = fontObj.render('UNDO', True, BLUE, CYAN)
           textRectObj = textSurfaceObj.get_rect() 
           textRectObj.center = (100,650)
           
           #fontObj1 = pygame.font.Font("freesansbold.ttf",32)
           textSurfaceObj1 = fontObj.render('REPLAY', True, BLUE, CYAN)
           textRectObj1 = textSurfaceObj1.get_rect() 
           textRectObj1.center = (300,650)
           
           #fontObj2 = pygame.font.Font("freesansbold.ttf",32)
           textSurfaceObj2 = fontObj.render('BACK', True, BLUE, CYAN)
           textRectObj2 = textSurfaceObj2.get_rect() 
           textRectObj2.center = (500,650)
           
           #fontObj4 = pygame.font.Font("freesansbold.ttf",32)
           textSurfaceObj4 = fontObj.render('NEXT LEVEL', True, WHITE, WHITE)
           textRectObj4 = textSurfaceObj4.get_rect() 
           textRectObj4.center = (400,300)
    
           drawboard()
           
           flag=False
           for i in range(rows):
               for j in range(columns):
                   if isEmpty(i,j):
                       flag=True
           if flag==False:
              fontObj = pygame.font.Font("freesansbold.ttf",32)
              textSurfaceObj4 = fontObj.render('NEXT LEVEL', True, BLACK, WHITE)
              textRectObj4 = textSurfaceObj4.get_rect() 
              textRectObj4.center = (400,300)
              
           
           catx += ((1))
           if catx==800:
               catx=0
           cat1y += 1
           if cat1y==700:
               cat1y=0
    
           for event in pygame.event.get():
             
               if event.type == QUIT:
                   '''pygame.quit()
                   sys.exit()'''
                   done=True
               mouse=pygame.mouse.get_pos()
               click=pygame.mouse.get_pressed()


               
               if click[0]==1:
                   if flag==True:
                       dir=getBoxAtPixel(mouse[0],mouse[1])
                       if dir[0]==6:
                           undofn()
                       elif dir[0]==7:
                           grid=[]
                           undo=[]
                           makegrid(level)
                       elif dir[0]==8:
                           w3()
                       elif dir[0]!=9:
                           flip(dir)
                       
                   if flag==False:
                       if 300<mouse[0]<500 and 250<mouse[1]<350:
                           w4(level+1)
                   
           d.blit(textSurfaceObj, textRectObj)
           del fontObj
           d.blit(textSurfaceObj1, textRectObj1)
           d.blit(textSurfaceObj2, textRectObj2)
           d.blit(textSurfaceObj4, textRectObj4)
           d.blit(catImg, (catx, caty))
           d.blit(catImg,(cat1x,cat1y))
           pygame.display.update()
           
    def makegrid(level): 
        #global size
        global rows
        global columns
        global nreq
        global color
        global colore
        global grid
        global n
        #global empty
        #global undo
        #global d
        #warm up
        undo=[]
        grid=[]
        if level==1:
            n=1
            rows=2
            columns=4
            color=[[[0,0],[0,1]]]
            colore=[[0,2,1,0]]
            nreq=[]
        if level==2:
            n=1
            rows=4
            columns=4
            color=[[[2,0],[3,0],[3,1]]]
            colore=[[2,2,4,0]]
            nreq=[[1,1],[2,2],[1,2],[2,1]]
        if level==3:
            n=1
            rows=4
            columns=4
            color=[[[3,0]]]
            colore=[[3,1,4,0]]
            nreq=[]
        if level==4:
            n=2
            rows=5
            columns=4
            color=[[[0,0]],[[4,2]]]
            colore=[[0,1,1,0],[4,3,5,2]]
            nreq=[[0,2],[0,3],[4,0],[4,1]]  
        if level==5:
            n=1
            rows=4
            columns=4
            color=[[[3,0],[2,1]]]
            colore=[[2,1,4,0]]
            nreq=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,3],[3,1],[3,2]]
        if level==6:
            n=4
            rows=6
            columns=5
            color=[[[0,3]],[[0,4]],[[5,3]],[[5,4]]]
            colore=[[0,4,1,3],[0,5,1,4],[5,4,6,3],[5,5,6,4]]
            nreq=[]
        if level==7:
            n=3
            rows=8
            columns=6
            color=[[[0,0],[0,1],[1,0],[1,1]],[[7,0]],[[7,4],[7,5]]]
            colore=[[0,2,2,0],[7,1,8,0],[7,6,8,4]]
            nreq=[]
        if level==8:
            n=3
            rows=9
            columns=5
            color=[[[0,0],[1,0]],[[1,0]],[[1,1]]]
            colore=[[0,1,2,0],[0,2,1,1],[1,2,2,1]]
            nreq=[8,0]
        if level==9:
            n=4
            rows=4
            columns=3
            color=[[[0,0]],[[1,1]],[[3,0]],[[3,2]]]
            colore=[[0,1,10],[1,2,2,1],[3,1,4,0],[3,3,4,2]]
            nreq=[]
        if level==10:
            n=4
            rows=6
            columns=4
            color=[[[0,0]],[[1,0],[2,0]],[[3,0],[3,1]],[[5,3]]]
            colore=[[0,1,1,0],[1,1,3,0],[3,2,4,0],[5,4,6,3]]
            nreq=[]
        if level==11:
            n=5
            rows=7
            columns=6
            color=[[[0,3],[0,4],[1,4],[1,5]],[[2,2]],[[3,0],[4,0],[4,1],[4,2]],[[5,1],[5,3]]]
            colore=[[0,6,2,3],[2,3,3,2],[3,3,5,0],[5,2,6,1],[5,4,6,3]]
            nreq=[[0,0],[0,5]]
        if level==12:
            n=5
            rows=6
            columns=6
            color=[[[0,4]],[[1,5]],[[2,0]],[[2,2]],[[4,4]]]
            colore=[[0,5,1,4],[1,6,2,5],[2,1,3,0],[2,3,3,2],[4,5,5,4]]
            nreq=[[4,0],[4,1],[5,0],[5,1],[5,2],[5,3]]
        if level==13:
            n=5
            rows=8
            columns=6
            color=[[[1,2]],[[1,4]],[[3,5]],[[4,3]],[[6,1]]]
            colore=[[1,3,2,2],[1,5,2,4],[3,6,4,5],[4,4,5,3],[6,2,7,1]]
            nreq=[[0,5],[1,5],[6,5],[7,5]]
        if level==14:
            n=5
            rows=8
            columns=6
            color=[[[0,0]],[[0,4]],[[1,1],[2,1],[2,2]],[[4,5]],[[5,6]]]
            colore=[[0,1,1,0],[0,5,1,4],[1,3,3,1],[4,6,5,5],[5,5,6,4]]
            nreq=[[0,5],[1,2],[1,3],[1,5],[2,5],[7,1],[7,2],[7,3],[7,4],[7,5]]
        if level==15:
            n=5
            rows=5
            columns=5
            color=[[[2,0]],[[2,4]],[[3,1]],[[3,3]],[[4,2]]]
            colore=[[2,1,3,0],[2,5,3,4],[3,2,4,1],[3,4,4,3],[4,3,5,2]]
            nreq=[[0,0],[0,1],[0,2],[0,3],[1,1],[1,2],[1,3]]

        #grid=[[-1]*size]*size
        for i in range(rows):
            grid.append([])
            for j in range(columns):
                grid[i].append(-1)
        k=0
        for i in color:
            for j in i:
                p=j[0]
                q=j[1]
                grid[p][q]=k
            k+=1
        for i in nreq:
            grid[i[0]][i[1]]=-2
    
    def drawboard():
        global color
        global colore
        global rows
        global columns
        global nreq
        global grid
        global n
        global em,bg4,col0,col1,col2,col3,col4,col5
        #global empty
        #global undo
        global d
        for i in range(rows):
            for j in range(columns):
                if(grid[i][j]==-1):#empty tile
                    pygame.draw.rect(d, em,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==-2):#background color
                    pygame.draw.rect(d, bg4,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==0):#color0
                    pygame.draw.rect(d, col0,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==1):#color1
                    pygame.draw.rect(d, col1,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==2):#color2
                    pygame.draw.rect(d, col2,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==3):#color3
                    pygame.draw.rect(d, col3,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==4):#color4
                    pygame.draw.rect(d, col4,(20+j*55,20+i*55,50,50))
                if(grid[i][j]==5):#color5
                    pygame.draw.rect(d, col5,(20+j*55,20+i*55,50,50))
        #color 0
        for i in range(n):
            if i==0:
                col=col0
            elif i==1:
                col=col1
            elif i==2:
                col=col2
            elif i==3:
                col=col3
            elif i==4:
                col=col4
            elif i==5:
                col=col5
            pygame.draw.rect(d, col,(735,5+100*i,30,30))#up
            pygame.draw.rect(d, col,(765,35+100*i,30,30))#right
            pygame.draw.rect(d, col,(735,65+100*i,30,30))#down
            pygame.draw.rect(d, col,(705,35+100*i,30,30))#left
        
        
    def getBoxAtPixel(x, y):
         for i in range(n):
             if x>735 and x<735+30 and y>100*i+5 and y<100*i+35:
                 return [i,1]
             elif x>765 and x<765+30 and y>100*i+35 and y<100*i+65:
                 return [i,2]
             elif x>735 and x<735+30 and y>100*i+65 and y<100*i+95:
                 return [i,3]
             elif x>705 and x<705+30 and y>100*i+35 and y<100*i+65:
                 return [i,4]
         #UNDO
         if x>70 and x<130 and y>650-16 and y<650+16:
             return [6,0]
         if x>300-30 and x<300+30 and y>650-16 and y<650+16:
             return [7,0]
         if x>500-30 and x<500+30 and y>650-16 and y<650+16:
             return [8,0]
         return [9,0]
    
    def flip(dir):
        global rows
        global columns
        global color
        global colore
        global grid
        global nreq
        global undo
        global d
        y=dir[0]
        dir=dir[1]
        j=color[y]
        k=colore[y]
    
        for i in j:
            a=i[0]
            b=i[1]
            
            if(dir==1):
                t=2*k[0]-a-1
                if not isEmpty(t,b):
                    #beep
                    return
            if(dir==2):
                t=2*k[1]-b-1
                if not isEmpty(a,t):
                    #beep
                    return
            if(dir==3):
                t=2*k[2]-a-1
                if not isEmpty(t,b):
                    #beep
                    return
            if(dir==4):
                t=2*k[3]-b-1
                if not isEmpty(a,t):
                    #beep
                    return
        p=[]
        for i in j:
            a=i[0]
            b=i[1]
            if(dir==1):
                t=2*k[0]-a-1
                p.append([t,b])
                grid[t][b]=y
            if(dir==2):
                t=2*k[1]-b-1
                p.append([a,t])
                grid[a][t]=y
            if(dir==3):
                t=2*k[2]-a-1
                p.append([t,b])
                grid[t][b]=y
            if(dir==4):
                t=2*k[3]-b-1
                p.append([a,t])
                grid[a][t]=y
        while(len(p)!=0):
            j.append(p.pop(0))
        if dir==1:
            k[0]=2*k[0]-k[2]
        elif dir==2:
            k[1]=2*k[1]-k[3]
        elif dir==3:
            k[2]=2*k[2]-k[0]
        elif dir==4:
            k[3]=2*k[3]-k[1]
      
        undo.append([y,dir])
        
    def isEmpty(a,b):
        global rows
        global columns
        if(a<rows and a>=0 and b>=0 and b<columns):
            if(grid[int(a)][int(b)]==-1):
                return 1
        return 0
    
    def undofn():
        global rows
        global columns
        global color
        global colore
        global nreq
        global grid
        global undo
        
        if len(undo)!=0:
            u=undo.pop()
        else:
            return
        #s=[]
        c=u[0]
        u=u[1]
        l=int(len(color[c])/2)
        
        if u==1:
            colore[c][0]=(colore[c][0]+colore[c][2])/2
            colore[c][0]=int(colore[c][0])
            
        if u==2:
            colore[c][1]=(colore[c][1]+colore[c][3])/2
            colore[c][1]=int(colore[c][1])
            
        if u==3:
            colore[c][2]=(colore[c][0]+colore[c][2])/2
            colore[c][2]=int(colore[c][2])
            
        if u==4:
            colore[c][3]=(colore[c][1]+colore[c][3])/2
            colore[c][3]=int(colore[c][3])
            
        p=len(color[c])
        for i in range(l,p):
            grid[color[c][i][0]][color[c][i][1]]=-1
        for i in range(l,p):
            color[c].pop()
            
    if _name_ == '_main_':
        main(level)
    
    pygame.quit()
    
w1()
