from kivy.app import App
from kivy.uix.floatlayout import FloatLayout #Tela Float Layout
from kivy.uix.screenmanager import ScreenManager, Screen #Controle das Telas
from kivy.uix.image import Image #Importa Imagens
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.animation import Animation
from random import random
from Reg_players import Rank, BancodeDadosPlayers
from reg_pont import Pont, BancodeDadosPoints

Builder.load_string('''
<CustomLayout>
    canvas.before:
        BorderImage:
            texture: self.background_image.texture
            pos: self.pos
            size: self.size
''')

class Manager(ScreenManager): #Classe para Manuseamente das Telas
    pass

class Menu(Screen): #Classe para controle da tela 'Menu'
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.som_menu = SoundLoader.load('Audio/Menu/Musica_de_Fundo.mp3')
        self.som_menu_volume = 0.05
        self.som_menu.play()
        self.som_menu.loop = True

    def controla_som(self,situacao):
        if situacao:
            self.som_menu.volume = 0.05
        else:
            self.som_menu.volume = 0
    
    # Método chamado pelo envento do Botão sair
    def leave(self):
        App.get_running_app().stop()
        self.som_menu.volume = 0

class Game(Screen): #Classe para controle da tela 'Game'
    obstacles = []
    def on_enter(self,*args):
        self.i = 0
        self.ids.score.text = '0'
        Clock.schedule_interval(self.update,1/30)
        Clock.schedule_interval(self.putObstacle,1.5)
    def update(self,*args):
        self.ids.player.speed += -self.height*1/30 
        self.ids.player.y += self.ids.player.speed *2* 1/30 #altera a posição em y considerando o dt, 1/30
        if self.ids.player.y < 80:
            self.ids.player.y = 80
        elif self.playerCollided():
            self.gameOver()
            self.importa_pontos()
        elif self.playerCollidedMid() and self.ids.player.y < 300:
            self.importa_pontos()
            self.gameOver()
        elif self.ids.player.y > 400:
            self.gameOver()
        for obstacle in self.obstacles:
            if self.ids.player.x > obstacle.x + 100:
                self.pontos()
    
    def pontos(self):
        self.i += 1
        j = str(self.i)
        self.ids.score.text = j
        
    def importa_pontos(self):
        pontos = int(self.ids.score.text)
        name = ''
        em = ''
        SignUp().pegapont(name, em, pontos)
    
    def putObstacle(self,*args):
        obstacle = Obstacle(x=self.width,height=500)
        self.add_widget(obstacle)
        self.obstacles.append(obstacle)
    
    def on_pre_enter(self,*args):
        self.ids.player.y = self.height/50 #valor a ser alterado
        self.ids.player.speed = 0
        
    def gameOver(self,*args):
        Clock.unschedule(self.update,1/30) #para de funcionar a gravidade na tela GameOver
        Clock.unschedule(self.putObstacle,1)
        App.get_running_app().root.current = 'gameOver'
        for obs in self.obstacles:
            obs.animation.cancel(obs)
            self.remove_widget(obs)
        self.obstacles = []

    def collidedUp(self,wid1,wid2):
        r1x = float(wid1.x)
        r1y = float(wid1.y)
        r2x = float(wid2.x)
        r2y = float(wid2.y)
        r1w = float(wid1.width)
        r1h = float(wid1.height)
        r2w = float(wid2.width)
        r2h = float(wid2.height)
        
        if (0 <= r1y <= r2y + 300 and r2x <= r1x + 300 <= r2x + 100 ):
            return True
        else:
            return False
            
    def collidedMid(self,wid1,wid2):
        r1x = float(wid1.x)
        r1y = float(wid1.y)
        r2x = float(wid2.x)
        r2y = float(wid2.y)
        r1w = float(wid1.width)
        r1h = float(wid1.height)
        r2w = float(wid2.width)
        r2h = float(wid2.height)
        
        if (r2x <= r1x + 160 <= r2x + 100):
            return True
        else:
            return False
        
    def playerCollided(self):
        collided = False
        for obstacle in self.obstacles:
            if self.collidedUp(self.ids.player,obstacle):
                collided = True
                break
        return collided
    
    def playerCollidedMid(self):
        collided = False
        for obstacle in self.obstacles:
            if self.collidedMid(self.ids.player,obstacle):
                collided = True
                break
        return collided
        
    def on_touch_down(self,*args):
        self.ids.player.speed = self.height*0.63 #Altura que o Player Pula = 0.55*altura da resoluçãoclass Game(Screen): #Classe para controle da tela 'Game'

class GameOver(Screen):
    def on_enter(self):
        da = BancodeDadosPoints()
        self.ids.score.text = str(da.pega_ponto())

class SignUp(Screen):

    # Método que armazena a pontuação.
    def pegapont(self,name,em,ponto):
        da = BancodeDadosPoints()
        db = BancodeDadosPlayers()
        self.nome = db.peganome()
        self.email = db.pegaemail()
        self.ponto = ponto
        pont = Pont(None,self.nome, self.email, self.ponto)
        da.novoPlayer(pont)
        App.get_running_app()
# função que registra um jogador e sua pontuação
    def Registrar(self):
        db = BancodeDadosPlayers()
        nome = self.ids.n1.text
        email = self.ids.n2.text
        new_player = Rank(None,nome,email)
        db.novoPlayer(new_player)
        App.get_running_app()
        
class Options(Screen): #Classe para controle da Tela "Options"
    pass

class Characters(Screen):
    pass

class Themes(Screen):
    pass

class Credits(Screen):
    pass

class Ranking(Screen):
    pass

class Obstacle(Widget):
    color = ListProperty([0.3,0.2,0.2,1])
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.animation = Animation(x=-self.width,duration=3)
        self.animation.bind(on_complete=self.vanish)
        self.animation.start(self)
    
    def vanish(self,*args):
        gameScreen = App.get_running_app().root.get_screen('game')
        gameScreen.remove_widget(self) 
        gameScreen.obstacles.remove(self)
    
class Player(Image):
    speed = NumericProperty(0)

class JogodinossauroApp(App):
    def build(self):
        pass
        
if __name__ == '__main__': #Certifica que o programa nao roda automaticamente
    JogodinossauroApp().run()
