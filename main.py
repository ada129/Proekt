import pygame
import os
from vibor import Vibor
from start import Start
from saund import Saund
from  cursor import Cursor
from Progress import Progress
pygame.init()
size=wight,height=480,680
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Доктор смерть")
pygame.display.set_icon(pygame.image.load("ikonka_igry.png"))
s=Saund(wight/1.1,height/14)
st=Start(wight,height)
fprog=open("prog.txt","r+")
fnum=open("number.txt","r+")
fork=0
num=0
if os.path.getsize("number.txt")!=0:
          num=int(fnum.read(1))
if os.path.getsize("prog.txt")!=0:
          fork=int(fprog.read(1))
flevel=open("level.txt","r+")
level=flevel.read(1)          
p=Progress(int(level),fork,wight,height)
cur=Cursor(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
text=pygame.font.SysFont("arial",30)
kerst=Vibor("m_krest_12.png",60,height/13,0)
m=pygame.sprite.Group()
text_setia=text.render("Вы хотите переиграть серию " + level + " ?",True,(128,0,0))
text_sets=text.render("Вы хотите перезапустить сезон ?",True,(128,0,0))
yes=Vibor("da.png",100,height/2 + 100,0)
no=Vibor("net (1).png",350,height/2+100,0)
sd=pygame.mixer.Sound("saund/door-knock-front-door_fyxsefvo.ogg")
sm=pygame.mixer.Sound("saund/store-entrance-bell_m1bp86nu.ogg")
sb=pygame.mixer.Sound("saund/shum-tolpy.ogg")
stel=pygame.mixer.Sound("saund/02443.ogg")
volum=1
anim=0
animwait=[pygame.image.load("gif-splitter (1)/1.png"),pygame.image.load("gif-splitter (1)/2.png"),
          pygame.image.load("gif-splitter (1)/3.png"),pygame.image.load("gif-splitter (1)/4.png"),
          pygame.image.load("gif-splitter (1)/5.png"),pygame.image.load("gif-splitter (1)/6.png"),
          pygame.image.load("gif-splitter (1)/7.png"),pygame.image.load("gif-splitter (1)/8.png"),
          pygame.image.load("gif-splitter (1)/9.png"),pygame.image.load("gif-splitter (1)/10.png"),
          pygame.image.load("gif-splitter (1)/11.png"),pygame.image.load("gif-splitter (1)/12.png"),
          pygame.image.load("gif-splitter (1)/13.png"),pygame.image.load("gif-splitter (1)/14.png"),
          pygame.image.load("gif-splitter (1)/15.png"),pygame.image.load("gif-splitter (1)/16.png"),
          pygame.image.load("gif-splitter (1)/17.png"),pygame.image.load("gif-splitter (1)/18.png")]
clock= pygame.time.Clock()
flagm=False
flagp=False
flagrec=False
flagrec1=False
flagfive=False
flagone=False
flagtwo=False
flagthree=False
flagfour=False
def one():
    global num
    global level
    global fork
    if num<=1:
        screen.blit(pygame.image.load("fon_vaska.png"),(0,0))
        screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"),(70,250))
        if num==0:
            screen.blit(text.render("Весной 2000 года соверешено жесткое убийство", True, (128, 0, 0)), (80, 100))
        else:
            screen.blit(text.render("В квартире на Васильевском острове был обнаружен труп пожилой женщины бывшей примы балерины Елизаветы Петровны Пирсовой", True, (128, 0, 0)), (80, 100))
    elif num==2:
        screen.blit(pygame.image.load("fon_kvartira.png"),(0,0))
        screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70, 250))
        screen.blit(text.render("На ее шеи преступники  затянули капроновые чулки. Из квартиры пропали ценные вещи.", True, (128, 0, 0)), (80, 100))
    elif num>2 and num<5:
        screen.blit(pygame.image.load("fon_kvartira_i_sledovatel.png"),(0,0))
        screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
        if num==3:
            screen.blit(text.render("Убийцы не оставили ни одного следа, ни одного отпечатка пальцев.", True, (128, 0, 0)), (80, 100))
        elif num==4:
            screen.blit(text.render("Я заметил странное, что на двери нет следов взлома. Кому могла открыть дверь осторожная женщина?", True, (128, 0, 0)), (80, 100))
    elif num==5:
            screen.blit(pygame.image.load("fon_kvartira_i_sledovatel.png"), (0, 0))
            screen.blit(pygame.image.load("m_okno_vybora .png"),(60,400))
            screen.blit(text.render("опросить соседей",True,(128,0,0)),(62,400))
            screen.blit(pygame.image.load("m_okno_vybora .png"),(60,500))
            screen.blit(text.render("провести обыск", True, (128, 0, 0)), (62,500))
    elif num==6:
        screen.fill((0, 0, 0))
        if fork==1:
          screen.blit(text.render("Меня тоже обокрали, представлеяте ко мне пришел врач, сделал укол и я уснула. Просыпаюсь, а в квартре ничего нет. Ходят тут кто хочет. Вот поэтому так и случается.", True, (128, 0, 0)), (80,200))
          screen.blit(pygame.image.load("sumashedshaya_babka_2.png"),(100,475))
        else:
            screen.blit(text.render("Пропал антиквариант: дорогая ваза", True, (128, 0, 0)), (80, 200))
            screen.blit(pygame.image.load("vaza.png"),(150,350))
    elif num==7:
        s.adjustment(0.5)
        stel.play(1)
        screen.blit(pygame.image.load("m_Советский_телефон_ТА-68.jpg"),(0,0))
        screen.blit(pygame.image.load("m_okno_vybora .png"), (70, 400))
        screen.blit(text.render("отправиться на вызов", True, (128, 0, 0)), (73,400))
    else:
        if num==8:
           stel.stop()
           s.adjustment(volum)
           level=2
           p.update(level-1,0)
           screen.blit(p.image,(0,0))
    screen.blit(pygame.image.load("krest_12.png"), (10, 20))
    if num==9:
       screen.blit(pygame.image.load("konets.png"),(0,0))
       fprog.write(str(fork))
def two():
    global num
    global fork
    if num==0:
        screen.blit(pygame.image.load("fon_kvartira_babaka_2.png"),(0,0))
        screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70, 250))
        screen.blit(text.render("В квартире была убита Зоя Тихоновна Степанова, человек заслуженный и известный. Ее удавили чулком. Пропали ордена и медали.", True, (128, 0, 0)), (80, 270))
    elif num>=1 and num<=5:
        if num%2!=0:
           screen.blit(pygame.image.load("fon_kvartira_babaka_2.png"), (0, 0))
           screen.blit(pygame.image.load("sledovatel_2.png"), (50,80))
           screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
           if num==1:
               screen.blit(text.render("Очень странно, потерпевшая снова сама впустила в квартиру.", True, (128, 0, 0)), (80,420))
           elif num==3:
               screen.blit(text.render("Кто мог приходить к убитой", True, (128, 0, 0)), (80,420))
           else:
               screen.blit(text.render("юля тут писать", True, (128, 0, 0)), (80,420))
        else:
           screen.blit(pygame.image.load("kadr_babka_blondinka.png"),(0,-100))
           screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
           if num==2:
                screen.blit(text.render("Она всегда была осторожной и никогда не впустила бы чужого в квартиру", True, (128, 0, 0)), (80, 420))
           else:
               screen.blit(text.render("Она часто болела, кроме меня и врача больше было некому.", True, (128, 0, 0)), (80,420))
    elif num>=6 and num<=10 :
           if num%2==0:
             screen.blit(pygame.image.load("kadr_magazin_antikvariat.png"),(0,0))
             screen.blit(pygame.image.load("prodavets_antikvariata_2.png"),(100,70))
             screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
             if num==6:
                s.adjustment(0.3)
                sm.play(1)
                screen.blit(text.render("...", True, (128, 0, 0)), (80, 420))
             elif num==8:
                 screen.blit(text.render("Здравствуйте, чем могу помочь?", True, (128, 0, 0)), (80, 420))
             else:
                 screen.blit(text.render("Нет, первы раз вижу, такие дорогие вещи я бы не забыл. Еще могу чем нибудь помочь?", True, (128, 0, 0)), (80, 420))
           else:
               if num!=9:
                  screen.blit(pygame.image.load("kadr_magazin_antikvariat.png"),(0,0))
                  screen.blit(pygame.image.load("sledovatel_2.png"),(1,70))
                  screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
                  if num==7:
                      screen.blit(text.render("К вам не поступал антиквариант: дорогая ваза, ордены и медали?", True, (128, 0, 0)), (80, 420))
               else:
                   screen.fill((0,0,0))
                   screen.blit(text.render("показать продавцу", True, (128, 0, 0)), (80,200))
                   screen.blit(pygame.image.load("vaza.png"), (150, 350))
           if num>6:
             sm.stop()
             s.adjustment(volum)
    elif num==11:
         level=3
         p.update(level-1,fork)
         screen.blit(p.image,p.rect)
    screen.blit(pygame.image.load("krest_12.png"), (10, 20))
    if num==12:
        screen.blit(pygame.image.load("konets.png"),(0,0))
def three():
    global level
    global fork
    global num
    if num>=0 and num<=4:
       screen.blit(pygame.image.load("fon_morg.png"),(0,0))
       if num%2==0:
           screen.blit(pygame.image.load("katya_vrach_4.png"),(100,70))
       else:
           screen.blit(pygame.image.load("sledovatel_2.png"),(50,70))
       screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
       if num==0:
           screen.blit(text.render("Войдите", True, (128, 0, 0)), (80, 420))
       elif num==1:
           screen.blit(text.render("От чего умерли потерпевшие?", True, (128, 0, 0)), (80, 420))
       elif num==2:
           screen.blit(text.render("Пожилые женщины умерли от острой сердечной недостаточности", True, (128, 0, 0)), (80, 420))
       elif num==3:
           screen.blit(text.render("Что нибудь еще есть?", True, (128, 0, 0)), (80, 420))
       elif num==4:
           screen.blit(text.render("На локтевом сгибе есть укол.", True, (128, 0, 0)), (80, 420))
       if num==0:
           sd.play(1)
           s.adjustment(0.3)
       else:
           s.adjustment(volum)
           sd.stop()
    elif num==5:
        screen.blit(pygame.image.load("kadr_mnogoetazhka.png"),(0,0))
        screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70, 250))
        screen.blit(text.render("Запутанное дело, обе женщины были здоровы и никогда не образали к врачам. Может все дело в уколе. Но кто сделал этот укол?", True, (128, 0, 0)), (80, 270))
    elif num>=6 and num<=9:
        screen.blit(pygame.image.load("kadr_mnogoetazhka.png"),(0,0))
        if num%2==0:
           screen.blit(pygame.image.load("Babki_spletnitsy.png"),(0,100))
           screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
           if num==6:
               screen.blit(text.render("Что-то страшное происходит, убивают старушек, ради выгоды, хотят наши квартиры получить.", True, (128, 0, 0)), (80, 420))
           else:
               screen.blit(text.render("Никого мы не знаем, но убили ее из-за богатсва и квартиры!!!", True, (128, 0, 0)), (80, 420))
        else:
            screen.blit(pygame.image.load("sledovatel_yulya.png"),(100,70))
            screen.blit(pygame.image.load("m_dialogovoe_okno (1).png"), (70,400))
            if num==7:
               screen.blit(text.render("Здравствуйте, вы знали Фокину?", True, (128, 0, 0)), (80, 420))
            else:
                screen.blit(text.render("Версия про квартиру и деньги отпадает сразу, так как особой выгоды от этого убицы не получают. Но что же вкалывают пенсионеркам?", True, (128, 0, 0)), (80, 420))
        if num == 6:
            sb.play(1)
            s.adjustment(0.3)
        else:
            sb.stop()
            s.adjustment(volum)
    elif num==10:
         level=4
         p.update(level-1,fork)
         screen.blit(p.image,p.rect)
    screen.blit(pygame.image.load("krest_12.png"), (10, 20))
    if num==11:
        screen.blit(pygame.image.load("konets.png"), (0, 0))
def draw():
    global  anim
    if anim+1>=19:
        anim=0
    screen.blit(animwait[anim],(0,305))
    screen.blit(pygame.image.load("krest_12.png"),(10,20))
    screen.blit(text.render("Серия в разработке",True,(128,0,0)),(125,200))
    anim+=1
screen.blit(st.image,st.rect)
screen.blit(s.image,s.rect)
pl=False
running=True
while running:
    clock.tick(18)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT:
               if volum>=0.1:
                   volum-=0.1
                   s.adjustment(volum)
             elif event.key==pygame.K_RIGHT:
                  if volum<=1:
                     volum+=0.1
                     s.adjustment(volum)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if pygame.mouse.get_pos()[1]>=21 and pygame.mouse.get_pos()[1]<=61 and pygame.mouse.get_pos()[0]>=401 and pygame.mouse.get_pos()[0]<=449 :
                cur.Tip_off(True)
                s.update()
            elif  pygame.mouse.get_pos()[0]>=82 and pygame.mouse.get_pos()[0]<=437 and pygame.mouse.get_pos()[1]>199 and pygame.mouse.get_pos()[1]<341:
                    st.p(True)
                    pl=True
                    if not flagm:
                        cur.Tip_off(True)
                    if level=="2":
                         m.add(Vibor("krest_12.png", 110, 195,1), Vibor("2_mini.png", 240, 190,2), Vibor("krest_12.png", 380, 190,3),
                                     Vibor("krest_12.png", 170, 300,4), Vibor("krest_12.png", 300, 300,5),
                                     Vibor("m_lupa_5.png", 240, 400,6),
                                     Vibor("strelochka.png", 240, 500,7))
                    elif level=="3":
                         m.add(Vibor("krest_12.png", 110, 195,1), Vibor("krest_12.png", 240, 190,2), Vibor("nomer_3.png", 380, 190,3),
                               Vibor("krest_12.png", 170, 300,4), Vibor("krest_12.png", 300, 300,5),
                               Vibor("m_lupa_5.png", 240, 400,6),
                               Vibor("strelochka.png", 240, 500,7))
                    elif level=="4":
                         m.add(Vibor("krest_12.png", 110, 195,1), Vibor("krest_12.png", 240, 190,2), Vibor("krest_12.png", 380, 190,3),
                               Vibor("nomer_4.png", 170, 300,4), Vibor("krest_12.png", 300, 300,5),
                               Vibor("m_lupa_5.png", 240, 400,6),
                               Vibor("strelochka.png", 240, 500,7))
                    elif level=="5":
                         m.add(Vibor("krest_12.png", 110, 195,1), Vibor("krest_12.png", 240, 190,2),Vibor("krest_12.png", 380, 190,3),
                               Vibor("krest_12.png", 170, 300,4), Vibor("nomer_5.png", 300, 300,5),
                               Vibor("m_lupa_5.png", 240, 400,6),
                               Vibor("strelochka.png", 240, 500,7))
                    else:
                        m.add(Vibor("1_mini.png", 110, 195,1), Vibor("krest_12.png", 240, 190,2),Vibor("krest_12.png", 380, 190,3),
                              Vibor("krest_12.png", 170, 300,4), Vibor("krest_12.png", 300, 300,5),
                              Vibor("m_lupa_5.png", 240, 400,6),
                              Vibor("strelochka.png", 240, 500,7))
                    flagm=True
            elif flagm and pygame.mouse.get_pos()[0]>=181 and pygame.mouse.get_pos()[0]<=268 and pygame.mouse.get_pos()[1]>=357 and pygame.mouse.get_pos()[1]<429:
                 cur.Tip_off(True)
                 flagp=True
                 flagm=False
                 print(pygame.mouse.get_pos())
            elif flagp and pygame.mouse.get_pos()[1]>=29 and pygame.mouse.get_pos()[1]<=67 and pygame.mouse.get_pos()[0]>=29 and pygame.mouse.get_pos()[0]<=75:
                 cur.Tip_off(True)
                 flagp=False
                 flagm=True
            elif flagm and pygame.mouse.get_pos()[0]>=215 and pygame.mouse.get_pos()[0]<=282 and pygame.mouse.get_pos()[1]>=492 and pygame.mouse.get_pos()[1]<=555:
                 cur.Tip_off(True)
                 flagm=False
                 flagrec=True
                 flagrec1=True
            elif flagrec and flagrec1:
                 if pygame.mouse.get_pos()[1]>=425 and pygame.mouse.get_pos()[1]<=513 and pygame.mouse.get_pos()[0]>=65 and pygame.mouse.get_pos()[0]<=138:
                    cur.Tip_off(True)
                    if int(level)>1:
                       level=str(int(level)-1)
                       flevel.seek(0)
                       flevel.truncate()
                       flevel.write(level)
                       m.update(int(level))
                    flagrec=False
                    flagm=True
                    flagrec1=False
                 else:
                     if pygame.mouse.get_pos()>=(315,436) and pygame.mouse.get_pos()<=(397,499):
                         flagrec1=False
            elif flagrec and not flagrec1:
                if pygame.mouse.get_pos() >= (65,425) and pygame.mouse.get_pos() <= (138,513):
                    fprog.seek(0)
                    fprog.truncate()
                    flevel.seek(0)
                    flevel.truncate()
                    flevel.write("1")
                    m.update(int(level))
                    flagrec=False
                    flagm=True
                else:
                    if pygame.mouse.get_pos()>=(315,436) and pygame.mouse.get_pos()<=(397,499):
                        flagrec=False
                        flagm=True
            elif flagm:
                 print(pygame.mouse.get_pos())
                 if level=="1" and pygame.mouse.get_pos()[0]>=81 and pygame.mouse.get_pos()[0]<=145 and pygame.mouse.get_pos()[1]>=166 and pygame.mouse.get_pos()[1]<=219:
                     cur.Tip_off(True)
                     num=0
                     flagone=True
                     flagm=False
                 elif level=="2" and pygame.mouse.get_pos()[0]>=210 and pygame.mouse.get_pos()[0]<=276 and pygame.mouse.get_pos()[1]>=166 and pygame.mouse.get_pos()[1]<=219:
                     print(num)
                     flagtwo=True
                     flagm=False
                     cur.Tip_off(True)
                 elif level=="3" and pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[0]<=416 and pygame.mouse.get_pos()[1]>=166 and pygame.mouse.get_pos()[1]<=219:
                     cur.Tip_off(True)
                     flagthree=True
                     flagm=False
                 elif level=="4" and pygame.mouse.get_pos()[0]>=143 and pygame.mouse.get_pos()[0]<=207 and pygame.mouse.get_pos()[1]>=278 and pygame.mouse.get_pos()[1]<=335:
                     cur.Tip_off(True)
                     flagfour=True
                     flagm=False
                 elif level=="5" and pygame.mouse.get_pos()>=(265,265) and pygame.mouse.get_pos()<=(335,336):
                     cur.Tip_off(True)
                     flagfive=True
                     flagm=False
            elif (flagfive or flagfour) and pygame.mouse.get_pos()>=(36,67) and pygame.mouse.get_pos()<=(97,123) :
                     flagfour=False
                     cur.Tip_off(True)
                     flagfive=False
                     flagm=True
            elif flagone and pygame.mouse.get_pos()>=(21,47) and  pygame.mouse.get_pos()<=(80,102):
                     cur.Tip_off(True)
                     flagone=False
                     flagm=True
                     fnum.seek(0)
                     fnum.truncate()
                     fnum.write(str(num))
            elif flagone and pygame.mouse.get_pos()>=(90,319) and pygame.mouse.get_pos()<=(370,459) and num<4:
                 cur.Tip_off(True)
                 num+=1
            elif flagone and num==4 and pygame.mouse.get_pos()>=(90,469) and pygame.mouse.get_pos()<=(370,610):
                cur.Tip_off(True)
                num+=1
            elif pygame.mouse.get_pos() >= (93, 530) and pygame.mouse.get_pos() <= (408, 587) and flagone and num == 5:
                num += 1
                fork = 2
                fprog.write(str(fork))
                cur.Tip_off(True)
            elif flagone and num==5 and pygame.mouse.get_pos()>=(93,435) and  pygame.mouse.get_pos()<=(408,484):
                   num+=1
                   fork=1
                   fprog.write(str(fork))
                   cur.Tip_off(True)
            elif flagone and num==6 :
                 cur.Tip_off(True)
                 num+=1
            elif flagone and num==7 and pygame.mouse.get_pos()>=(107,436) and pygame.mouse.get_pos()<=(412,481):
                 cur.Tip_off(True)
                 num+=1
            elif flagone and num==8:
                 cur.Tip_off(True)
                 num+=1
            elif flagone and num==9 and pygame.mouse.get_pos()>=(78,340) and pygame.mouse.get_pos()<=(404,421):
                 num=0
                 cur.Tip_off(True)
                 flagone=False
                 flagm=True
                 flevel.seek(0)
                 flevel.truncate()
                 flevel.write("2")
                 m.update(level)
            elif flagtwo and num==0 and pygame.mouse.get_pos()>=(97,321) and pygame.mouse.get_pos()<=(375,452):
                 cur.Tip_off(True)
                 num+=1
            elif flagtwo and num>0 and num<6 and pygame.mouse.get_pos()>=(97,474) and pygame.mouse.get_pos()<=(375,607):
                cur.Tip_off(True)
                num+=1
            elif flagtwo and num>5 and num<11 and pygame.mouse.get_pos()>=(97,474) and pygame.mouse.get_pos()<=(375,607):
                cur.Tip_off(True)
                num+=1
            elif flagtwo and num==11 and pygame.mouse.get_pos()>=(27,138) and pygame.mouse.get_pos()<=(463,603):
                cur.Tip_off(True)
                num+=1
            elif flagtwo and num==12 and pygame.mouse.get_pos()>=(78,340) and pygame.mouse.get_pos()<=(404,421):
                num = 0
                cur.Tip_off(True)
                flagtwo=False
                flagm = True
                flevel.seek(0)
                flevel.truncate()
                flevel.write("3")
                m.update(level)
            elif flagthree and num>-1 and num<=4 and pygame.mouse.get_pos()>=(97,474) and pygame.mouse.get_pos()<=(375,607):
                cur.Tip_off(True)
                num+=1
            elif flagthree and num==5 and pygame.mouse.get_pos()>=(90,319) and pygame.mouse.get_pos()<=(370,459):
                num += 1
                if fork == 2:
                    num+=5
                cur.Tip_off(True)
            elif flagthree and num>5 and num<=9 and pygame.mouse.get_pos()>=(97,474) and pygame.mouse.get_pos()<=(375,607):
                num+=1
                cur.Tip_off(True)
            elif flagthree and num==10 and pygame.mouse.get_pos()>=(27,138) and pygame.mouse.get_pos()<=(463,603):
                 num+=1
                 cur.Tip_off(True)
            elif flagthree and num==11 and pygame.mouse.get_pos()>=(78,340) and pygame.mouse.get_pos()<=(404,421):
                num = 0
                cur.Tip_off(True)
                flagthree = False
                flagm = True
                flevel.seek(0)
                flevel.truncate()
                flevel.write("4")
                m.update(level)
        else:
            print(pygame.mouse.get_pos())
            st.p(False)
            cur.Tip_off(False)
    cur.update(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    #pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    screen.fill((0,0,0))
    if flagm:
        m.draw(screen)
    elif flagp:
        screen.blit(p.image,p.rect)
        screen.blit(kerst.image,kerst.rect)
    elif flagrec:
         if flagrec1:
            screen.blit(text_setia,text_setia.get_rect(center=(wight/2,height/2)))
         else:
             screen.blit(text_sets,text_sets.get_rect(center=(wight/2,height/2)))
         screen.blit(yes.image, yes.rect)
         screen.blit(no.image, no.rect)
    elif flagfive:
         draw()
    elif flagone and num<10:
        one()
    elif flagtwo:
        two()
    elif flagthree:
        three()
    elif flagfour:
        draw()
    else:
        screen.blit(st.image, st.rect)
    screen.blit(s.image, s.rect)
    screen.blit(cur.image, cur.rect)
    pygame.display.flip()
pygame.quit()
