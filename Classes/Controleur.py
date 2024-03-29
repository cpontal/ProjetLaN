
import pygame
from pygame.locals import *
pygame.init()
from Classes.Level import *
from Classes.Player import *
import time
import sys #module systeme
from Classes.Piece import *
from threading import Timer

Display_Width = 1024
Display_Height = 768

#==============================================================================#
#=============================== IMAGES =======================================#
"""Ajout des images menu"""
background = pygame.image.load("images/background.png").convert_alpha()
titre = pygame.image.load("images/titre.png").convert_alpha()
jouer0 = pygame.image.load("images/jouer.png").convert_alpha()
jouer = pygame.transform.scale(jouer0, (300, 100))
options0 = pygame.image.load("images/options.png").convert_alpha()
options = pygame.transform.scale(options0, (300, 100))
credits0 = pygame.image.load("images/credits.png").convert_alpha()
credits = pygame.transform.scale(credits0, (300, 100))
reinit0 = pygame.image.load("images/reinit.png").convert_alpha()
reinit = pygame.transform.scale(reinit0, (300, 100))
menu0 = pygame.image.load("images/menu.png").convert_alpha()
menu = pygame.transform.scale(menu0, (300, 100))
rejouer0 = pygame.image.load("images/rejouer.png").convert_alpha()
rejouer = pygame.transform.scale(rejouer0, (300, 100))
titreoptions = pygame.image.load("images/titreoptions.png").convert_alpha()
quitter0 = pygame.image.load("images/quitter.png").convert_alpha()
quitter = pygame.transform.scale(quitter0, (300, 100))
pause0 = pygame.image.load("images/pause.png").convert_alpha()
pause = pygame.transform.scale(pause0, (100, 100))
choixlvl = pygame.image.load("images/choixlvl.png").convert_alpha()
lvl_10 = pygame.image.load("images/1.png").convert_alpha()
lvl_1 = pygame.transform.scale(lvl_10, (300, 100))
lvl_20 = pygame.image.load("images/2.png").convert_alpha()
lvl_2 = pygame.transform.scale(lvl_20, (300, 100))
lvl_2_block0 = pygame.image.load("images/2block.png").convert_alpha()
lvl_2_block = pygame.transform.scale(lvl_2_block0, (300, 100))
lvl_30 = pygame.image.load("images/3.png").convert_alpha()
lvl_3 = pygame.transform.scale(lvl_30, (300, 100))
lvl_3_block0 = pygame.image.load("images/3block.png").convert_alpha()
lvl_3_block = pygame.transform.scale(lvl_3_block0, (300, 100))
empty0 = pygame.image.load("images/empty.png").convert_alpha()
empty = pygame.transform.scale(empty0, (400, 100))
retour0 = pygame.image.load("images/retour.png").convert_alpha()
retour = pygame.transform.scale(retour0, (300, 100))
rejouer0 = pygame.image.load("images/rejouer.png").convert_alpha()
rejouer = pygame.transform.scale(rejouer0, (300, 100))

# POUR TESTS
grille = pygame.image.load("images/grille.png").convert_alpha()

#==============================================================================#
#==============================================================================#

"""musique"""
##musique_jeux = pygame.mixer.music.load('music/musiqueenjeux.mp3')

#==============================================================================#
#============================= CLASSES MENUS ==================================#


# creation des variable de base
pygame.display.set_caption("CHICAGO ADVENTURE")
clock = pygame.time.Clock()
Display = pygame.display.set_mode((Display_Width,Display_Height))
global level_en_cours_numero
FPS = 60

# affiche menu principal
def Menu_Start():
    global level_en_cours_numero
    menuStart = True
    pygame.mixer.music.stop()

    while menuStart:
        positionSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if pla.collidepoint(positionSouris):
                    #Display.blit(play_en,(320,185)) # Image quand bouton enfoncé
                    pygame.display.update()
                    time.sleep(1)
                    Menu_niveau()

                if opt.collidepoint(positionSouris):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_options()

                if quit.collidepoint(positionSouris):
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        Display.blit(background,(0,0))
        titr = Display.blit(titre,(0,0))
        pla = Display.blit(jouer,(362,335))
        opt = Display.blit(options,(362,460))
        quit =  Display.blit(quitter,(362,580))
        pygame.display.flip()


# affiche menu pour choix niveau
def Menu_niveau():
    global level_en_cours_numero
    MenuOptions = True

    pygame.key.set_repeat(400,30)
    while MenuOptions:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if lvl1.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 0
                    GameLoop()

                f_high_lvl1 = open("high/lvl1.txt", "r")
                if int(f_high_lvl1.read()) >= 25:
                    if lvl2.collidepoint(posSouris):
                        pygame.display.update()
                        time.sleep(1)
                        level_en_cours_numero = 1
                        GameLoop()
                f_high_lvl1.close()

                f_high_lvl2 = open("high/lvl2.txt", "r")
                if int(f_high_lvl2.read()) >= 25:
                    if lvl3.collidepoint(posSouris):
                        pygame.display.update()
                        time.sleep(1)
                        level_en_cours_numero = 2
                        GameLoop()
                f_high_lvl2.close()

                if retourO.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_Start()

        Display.blit(background,(0,0))
        Display.blit(choixlvl,(0,0))
        retourO = Display.blit(retour,(50,600))

        dessous = pygame.Surface((300,200))
        dessous.fill( (0,0,0) )
        dessous.set_alpha(128)
        Display.blit(dessous,(50,400))
        Display.blit(dessous,(370,400))
        Display.blit(dessous,(690,400))


        lvl1 = Display.blit(lvl_1,(50,320))
        font = pygame.font.SysFont('verdanaprocondblack', 50)
        f_high_lvl1 = open("high/lvl1.txt", "r")
        high_lvl1 = font.render("Record : " + f_high_lvl1.read(),1,(255,255,255))
        Display.blit(high_lvl1, (50, 450))
        f_high_lvl1.close()

        f_high_lvl1 = open("high/lvl1.txt", "r")
        if int(f_high_lvl1.read()) >= 25:
            lvl2 = Display.blit(lvl_2,(370,320))
            f_high_lvl2 = open("high/lvl2.txt", "r")
            high_lvl2 = font.render("Record : " + f_high_lvl2.read(),1,(255,255,255))
            Display.blit(high_lvl2, (370, 450))
            f_high_lvl2.close()
        else:
            lvl2 = Display.blit(lvl_2_block,(370,320))
            lock = font.render("Requis : 25",1,(255,255,255))
            Display.blit(lock, (370, 450))
            lock = font.render("sur le niveau 1",1,(255,255,255))
            Display.blit(lock, (370, 510))
        f_high_lvl1.close()

        f_high_lvl2 = open("high/lvl2.txt", "r")
        if int(f_high_lvl2.read()) >= 25:
            lvl3 = Display.blit(lvl_3,(690,320))
            f_high_lvl3 = open("high/lvl3.txt", "r")
            high_lvl3 = font.render("Record : " + f_high_lvl3.read(),1,(255,255,255))
            Display.blit(high_lvl3, (690, 450))
            f_high_lvl3.close()
        else:
            lvl3 = Display.blit(lvl_3_block,(690,320))
            lock = font.render("Requis : 25",1,(255,255,255))
            Display.blit(lock, (690, 450))
            lock = font.render("sur le niveau 2",1,(255,255,255))
            Display.blit(lock, (690, 510))
        f_high_lvl2.close()

        pygame.display.flip()

# affichage menu options
def Menu_options():
    global level_en_cours_numero
    menuOptions = True
    msg_reinit_bool = False

    pygame.key.set_repeat(400,30)
    while menuOptions:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if CredO.collidepoint(mpos):
                    pygame.display.update()
                    time.sleep(1)
                    Credit()

                if ReinitO.collidepoint(mpos):
                    f_high_lvl = open("high/lvl1.txt", "w")
                    f_high_lvl.write('0')
                    f_high_lvl.close()
                    f_high_lvl = open("high/lvl2.txt", "w")
                    f_high_lvl.write('0')
                    f_high_lvl.close()
                    f_high_lvl = open("high/lvl3.txt", "w")
                    f_high_lvl.write('0')
                    f_high_lvl.close()
                    msg_reinit_bool = True

                if MenuO.collidepoint(mpos):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_Start()

        Display.blit(background,(0,0))
        Display.blit(titreoptions,(0,0))
        CredO = Display.blit(credits,(362,335))
        ReinitO = Display.blit(reinit,(362,460))
        MenuO =  Display.blit(menu,(362,580))
        if msg_reinit_bool == True:
            font = pygame.font.SysFont('verdanaprocondblack', 50)
            msg_reinit = font.render("Scores réinitialisés",1,(255,255,255))
            Display.blit(msg_reinit, (10, 200))
        pygame.display.flip()

# affiche credits
def Credit():
    global level_en_cours_numero
    menuCredits = True

    pygame.key.set_repeat(400,30)
    while menuCredits:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.display.update()
                    time.sleep(1)
                    Menu_options()


        Display.blit(background,(0,0))
        dessous = pygame.Surface((1024,768))
        dessous.fill( (0,0,0) )
        dessous.set_alpha(128)
        Display.blit(dessous,(0,0))

        font = pygame.font.SysFont('verdanaprocondblack', 50)
        text4 = font.render("Developpement : Elias",1,(255,255,255))
        Display.blit(text4, (100, 80))
        text1 = font.render("\"Chef\" de projet : Corentin",1,(255,255,255))
        Display.blit(text1, (100, 160))
        text2 = font.render("Developpement : Benjamin",1,(255,255,255))
        Display.blit(text2, (100, 240))
        text3 = font.render("Graphisme : Lucas",1,(255,255,255))
        Display.blit(text3, (100, 320))
        text5 = font.render("Developpement : Jules",1,(255,255,255))
        Display.blit(text5, (100, 400))
        text6 = font.render("Merci d'avoir joué",1,(255,255,255))
        Display.blit(text6, (550, 580))
        pygame.display.flip()

# affiche Menu_Victoire
def Menu_Victoire():
    global level_en_cours_numero
    MenuVictoire = True


    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiquevictoire.mp3')
    pygame.mixer.music.play(-1)

    pygame.key.set_repeat(400,30)
    while MenuVictoire:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if rejouerV.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    GameLoop()

                if menuV.collidepoint(posSouris):
                    pygame.display.update()
                    time.sleep(1)
                    Menu_Start()

        Display.blit(background,(0,0))

        font = pygame.font.SysFont('verdanaprocondblack', 50)
        scoreFinal = font.render("Score : " + str(score) + " pts",1,(255,255,255))
        Display.blit(scoreFinal, (360, 20))

#high score check
        str_lvl = level_en_cours_numero + 1
        str_lvl = str(str_lvl)
        file = "high/lvl" + str_lvl + ".txt"
        f_high_lvl1 = open(file, "r")
        nb = int(f_high_lvl1.read())
        if nb <= score:
            if nb < 25 and score >= 25:
                font = pygame.font.SysFont('verdanaprocondblack', 50)
                highest = font.render("Niveau suivant débloqué",1,(255,255,255))
                Display.blit(highest, (360, 700))
            font = pygame.font.SysFont('verdanaprocondblack', 50)
            highest = font.render("Nouveau record !",1,(255,255,255))
            Display.blit(highest, (360, 100))
            f_high_lvl1 = open(file, "w")
            f_high_lvl1.write(str(score))

        f_high_lvl1.close()

        rejouerV = Display.blit(rejouer, (362, 335))
        menuV = Display.blit(menu, (362, 460))

        pygame.display.flip()

#==============================================================================#
#==============================================================================#

TIMEFINI = False
INT = 0
TIMEAFFICH = 180
six_secondes = 0
dix_secondes = 0
trente_secondes = 0

def timeout():
    global TIMEFINI
    TIMEFINI = True
    global TIMEAFFICH
    TIMEAFFICH = 180
    t = Timer(180.0, timeout)


def GameLoop():
    global level_en_cours_numero
    global score
    global bonus_actif

    GameRun = True
    GameOver = False
    score = 0
    bonus_actif = False

    t = Timer(180.0, timeout)
    #attention pas synchro avec affichage tps restant
    t.start()

    vitesseX = 0
    vitesseY = 0
    spacePressed = False
    player = Player()
    level_list = []
    # append ajouter element a la fin
    level_list.append(Level_1(player))
    level_list.append(Level_2(player))
    level_list.append(Level_3(player))

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiqueenjeux.mp3')
    pygame.mixer.music.play(-1)

    # grace a level_en_cours_numero(entier) on recupere la position dans la liste et donc le lvl dans la liste
    level_en_cours = level_list[level_en_cours_numero]

    player.level = level_en_cours
    sprite_bouge = pygame.sprite.Group()
    sprite_bouge.add(player)

    while GameRun:
################################################################################
        global INT
        global six_secondes
        global dix_secondes
        global trente_secondes
        global TIMEAFFICH
        INT = INT+1
        six_secondes += 1
        dix_secondes += 1
        trente_secondes += 1

        if INT == 59 :
            INT = 0
            TIMEAFFICH = TIMEAFFICH-1

        # TOUTES LES 10s
        if dix_secondes == 600:
            dix_secondes = 0
            level_en_cours.show_port(level_en_cours.level_portables)
        collision_portable = pygame.sprite.spritecollide(player,level_en_cours.portables_list,True)

        if collision_portable:
            score += 1

        if six_secondes == 360:
            six_secondes = 0
            level_en_cours.show_police(level_en_cours.level_police)
        collision_police = pygame.sprite.spritecollide(player,level_en_cours.police_list,True)

        if collision_police:
            score -= 5

        # TOUTES LES 30s
        if trente_secondes == 1800:
            trente_secondes = 0
            level_en_cours.show_bonus(level_en_cours.level_bonus)
        collision_bonus = pygame.sprite.spritecollide(player,level_en_cours.bonus_list,True)

        if collision_bonus:
            bonus_actif = True
            temps_bonus = 0

        if bonus_actif == True:
            temps_bonus += 1
            player.setGravite(0.1)

            if temps_bonus == 600:
                bonus_actif = False
                player.setGravite(0.5)

        while GameOver == True:
            time.sleep(1)
            pygame.mixer.music.stop()
            Menu_gameover()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                vitesseX = -5

            if event.key == K_RIGHT:
                vitesseX = 5

            if event.key == K_SPACE or event.key == K_UP:
                spacePressed = True
                vitesseY = -1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                vitesseX = 0
            if event.key == K_RIGHT:
                vitesseX = 0
            if (event.key == K_SPACE or event.key == K_UP) and spacePressed == True:
                player.saut(-10)
                spacePressed = False
                vitesseY = 1

        collision_player_platform = pygame.sprite.spritecollide(player,level_en_cours.platform_list,False)

        if collision_player_platform:
            auSol = False
            for plat in level_en_cours.platform_list:
                ecartGauche = player.rect.x + player.rect.width - plat.rect.x
                ecartDroite = plat.rect.x + plat.rect.width - player.rect.x
                ecartHaut = player.rect.y + player.rect.height - plat.rect.y
                ecartBas = plat.rect.y + plat.rect.height - player.rect.y
                if ecartGauche >= 50 and ecartGauche <= 55:
                    if ecartHaut > 35 and ecartBas > 30:
                        if vitesseX == 5:
                            vitesseX = 0
                if ecartDroite >= 25 and ecartDroite <= 30:
                    if ecartHaut > 35 and ecartBas > 30:
                        if vitesseX == -5:
                            vitesseX = 0
                if ecartHaut >= 20 and ecartHaut <= 35:
                    if ecartDroite > 30 and ecartGauche > 55:
                        if plat.type == "platform":
                            auSol = True
                        else:
                            player.setAuSol(True)
                            player.saut(-15)
                if ecartBas >= 0 and ecartBas <= 30:
                    if ecartDroite > 30 and ecartGauche > 55:
                        player.setAuSol(True)
                        player.saut(0)
            player.setAuSol(auSol)

        player.update(vitesseX,vitesseY)

        global TIMEFINI

        if TIMEFINI:
            time.sleep(1)
            GameOver = True
            pygame.mixer.music.stop()
            TIMEFINI=False
            Menu_Victoire()
        else :
            level_en_cours.draw(Display)
            sprite_bouge.draw(Display)

            dessous = pygame.Surface((1024,110))
            dessous.fill( (0,0,0) )
            dessous.set_alpha(128)
            Display.blit(dessous,(0,0))

            Display.blit(empty,(20,10))
            Display.blit(empty,(500,10))
            Display.blit(pause,(850,10))

            font = pygame.font.SysFont('verdana', 50)
            if TIMEAFFICH>30 :
                timerScreen = font.render("Timer : "+str(TIMEAFFICH)+" s",1,(255,255,255))
            else :
                timerScreen = font.render("Timer : "+str(TIMEAFFICH)+" s",1,(255,0,0))
            Display.blit(timerScreen, (50, 20))
            #attention pas synchro avec timer

            scoreScreen = font.render("Score : " + str(score) + " pts",1,(255,255,255))
            Display.blit(scoreScreen, (530, 20))
            if bonus_actif == True:
                font = pygame.font.SysFont('verdanaprocondblack', 50)
                actif = font.render("BONUS ACTIF",1,(255,255,255))
                Display.blit(actif, (600, 150))

            # rafraichi l'ecran
            pygame.display.flip()
            pygame.display.update()

            # gere les FPS
            clock.tick(FPS)
