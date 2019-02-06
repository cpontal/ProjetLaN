import pygame
pygame.init()


Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

gravite = 0.5

"""image pour mouvement perso"""
move_image1 = pygame.image.load("move/guy1.png").convert_alpha()
move_image2 = pygame.image.load("move/guy2.png").convert_alpha()
move_image3 = pygame.image.load("move/guy3.png").convert_alpha()
move_image4 = pygame.image.load("move/guy4.png").convert_alpha()
move_image5 = pygame.image.load("move/guy5.png").convert_alpha()
move_image6 = pygame.image.load("move/guy6.png").convert_alpha()


imageWidth = 78
imageHeight = 110
move_image1 = pygame.transform.scale(move_image1,(imageWidth,imageHeight))
move_image2 = pygame.transform.scale(move_image2,(imageWidth,imageHeight))
move_image3 = pygame.transform.scale(move_image3,(imageWidth,imageHeight))
move_image4 = pygame.transform.scale(move_image4,(imageWidth,imageHeight))
move_image5 = pygame.transform.scale(move_image5,(imageWidth,imageHeight))
move_image6 = pygame.transform.scale(move_image6,(imageWidth,imageHeight))

move_image1_r = pygame.transform.flip(move_image1, True, False)
move_image2_r = pygame.transform.flip(move_image2, True, False)
move_image3_r = pygame.transform.flip(move_image3, True, False)
move_image4_r = pygame.transform.flip(move_image4, True, False)

class Player(pygame.sprite.Sprite):
    def __init__(self):
##        super().__init__()
        self.auSol = True
        self.rect = move_image1.get_rect()
        self.rect.y = 50
        self.rect.x = 0
        self.vitesseX = 0
        self.vitesseY = 0
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed_init = 10
        self.animation_speed= self.animation_speed_init
        self.animation_list = [move_image1,move_image2,move_image3,move_image4]
        self.animation_list_r = [move_image1_r,move_image2_r,move_image3_r,move_image4_r]
        self.animation_position = 0
        self.animation_maximun = 3 #len(self.animation)-1
        self.image = move_image1
        self.update(1, 1)
        self.Gamelost = False



    # modifie le deplacement du joueur
    def update(self,vitesseX,vitesseY):
        self.vitesseX = vitesseX

        #savoir si le joueur est au plus bas ou pas
        if self.rect.y >= 580:
            self.rect.y = 580
            self.auSol = True
        else:
            self.auSol = False

        #change image par image
        self.animation_speed -= 1

        self.rect.x += self.vitesseX
        self.rect.y += self.vitesseY
        self.gravite()
        if self.animation_speed == 0:
            if vitesseX == 5: #le personnage avance
                self.image = self.animation_list[self.animation_position]
                self.animation_speed = self.animation_speed_init
                #si on est sur la dernière image on remet la première
                if self.animation_position == self.animation_maximun:
                    self.animation_position = 0
                else: #sinon on augmente l'image courante
                    self.animation_position += 1

            elif vitesseX == -5: #le personnage avance
                self.image = self.animation_list_r[self.animation_position]
                self.animation_speed = self.animation_speed_init
                #si on est sur la dernière image on remet la première
                if self.animation_position == self.animation_maximun:
                    self.animation_position = 0
                else: #sinon on augmente l'image courante
                    self.animation_position += 1
            elif vitesseY == -1:
                self.image = move_image6


            self.animation_speed = 10

        Display.blit(self.image,(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    # gere le saut
    def saut(self,vitesseY):
        self.vitesseY = vitesseY

    # gere la gravité
    def gravite(self):
        if self.vitesseY < 30 and self.auSol == False:
            self.vitesseY += gravite
