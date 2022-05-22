from tkinter import *              # importation de tout module neccessaire tkinter et randum
from tkinter import messagebox
import random
class Projet_2048:
    dico_couleur={                      # un dictionnaire de couleur pour que chaque case ai une couleur diff
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }
    color={                         # 
         '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }
    def __init__(self):             # initialisation de la grille vide et de l'interface tkinter comme nom de la page par exemple ; couleur 
        self.n=4
        self.fenetre=Tk()
        self.fenetre.title('Jeux 2048 Younes.B ')
        self.Jeux_2048Area=Frame(self.fenetre,bg= 'azure3')
        self.Projet_2048=[]
        self.taille_grille=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0
        for i in range(4):
            ligne=[]
            for j in range(4):
                l=Label(self.Jeux_2048Area,text='',bg='red',
                font=('red',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)
                ligne.append(l);
            self.Projet_2048.append(ligne)
        self.Jeux_2048Area.grid()
    def renverse(self):
        for ind in range(4):
            i=0             # i et j sont long larg de la grille 
            j=3
            while(i<j):
                self.taille_grille[ind][i],self.taille_grille[ind][j]=self.taille_grille[ind][j],self.taille_grille[ind][i]
                i+=1
                j-=1
    def transpose(self):
        self.taille_grille=[list(t)for t in zip(*self.taille_grille)]
    def Grille(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.taille_grille[i][j]!=0:
                    temp[i][cnt]=self.taille_grille[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.taille_grille=temp
    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.taille_grille[i][j] == self.taille_grille[i][j + 1] and self.taille_grille[i][j] != 0:
                    self.taille_grille[i][j] *= 2
                    self.taille_grille[i][j + 1] = 0
                    self.score += self.taille_grille[i][j]
                    self.merge = True
    def grille_randum(self):
        cellule=[]
        for i in range(4):
            for j in range(4):
                if self.taille_grille[i][j] == 0:
                    cellule.append((i, j))
        curr=random.choice(cellule)
        i=curr[0]
        j=curr[1]
        self.taille_grille[i][j]=2
    
    def grille_finals(self):
        for i in range(4):
            for j in range(3):
                if self.taille_grille[i][j] == self.taille_grille[i][j+1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if self.taille_grille[i+1][j] == self.taille_grille[i][j]:
                    return True
        return False
    def grille_couleur(self):
        for i in range(4):
            for j in range(4):
                if self.taille_grille[i][j]==0:
                    self.Projet_2048[i][j].config(text='',bg='azure4')
                else:
                    self.Projet_2048[i][j].config(text=str(self.taille_grille[i][j]),
                    bg=self.dico_couleur.get(str(self.taille_grille[i][j])),
                    fg=self.color.get(str(self.taille_grille[i][j])))
class Jeux_2048:
    def __init__(self,Jeux_2048panel):              # condition pour perdre et condition pour gagner
        self.Jeux_2048panel=Jeux_2048panel
        self.end=False                             # initialisation de end et won a false
        self.won=False
    def start(self): #creation de la grille aleatoirement grace a randum 
        self.Jeux_2048panel.grille_randum()
        self.Jeux_2048panel.grille_randum()
        self.Jeux_2048panel.grille_couleur()
        self.Jeux_2048panel.fenetre.bind('<Key>', self.link_keys)
        self.Jeux_2048panel.fenetre.mainloop()
    
    def link_keys(self,event):
        if self.end or self.won:         # condition pour arrete le jeu gagner ou grille remplie 
            return
        self.Jeux_2048panel.compress = False
        self.Jeux_2048panel.merge = False                        
        self.Jeux_2048panel.moved = False
        presed_key=event.keysym
        if presed_key=='Up':                        # creation des touche fleche pour se deplacer up down rigth left 
            self.Jeux_2048panel.transpose()
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.mergeGrid()
            self.Jeux_2048panel.moved = self.Jeux_2048panel.compress or self.Jeux_2048panel.merge 
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.transpose()
        elif presed_key=='Down':
            self.Jeux_2048panel.transpose()
            self.Jeux_2048panel.renverse()
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.mergeGrid()
            self.Jeux_2048panel.moved = self.Jeux_2048panel.compress or self.Jeux_2048panel.merge
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.renverse()
            self.Jeux_2048panel.transpose()
        elif presed_key=='Left':
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.mergeGrid()
            self.Jeux_2048panel.moved = self.Jeux_2048panel.compress or self.Jeux_2048panel.merge
            self.Jeux_2048panel.Grille()
        elif presed_key=='Right':
            self.Jeux_2048panel.renverse()
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.mergeGrid()
            self.Jeux_2048panel.moved = self.Jeux_2048panel.compress or self.Jeux_2048panel.merge
            self.Jeux_2048panel.Grille()
            self.Jeux_2048panel.renverse()
        else:
            pass
        self.Jeux_2048panel.grille_couleur()
        print(self.Jeux_2048panel.score)
        flag=0
        for i in range(4):
            for j in range(4):
                if(self.Jeux_2048panel.taille_grille[i][j]==2048):
                    flag=1
                    break 
        if(flag==1):
            self.won=True               # lorsque qu'une case sera egale a 2048 
            messagebox.showinfo('2048', message='Bravo vous avez gagné')
            print("Bravo")
            return
        for i in range(4):
            for j in range(4):
                if self.Jeux_2048panel.taille_grille[i][j]==0:
                    flag=1
                    break
        if not (flag or self.Jeux_2048panel.grille_final()):
            self.end=True                             # lorsque la grille est remplie donc perdu
            messagebox.showinfo('2048',' Perdu Dommage ')
            print("Perdu")
        if self.Jeux_2048panel.moved:
            self.Jeux_2048panel.grille_randum()
        
        self.Jeux_2048panel.grille_couleur()
    
Jeux_2048panel =Projet_2048()
Jeux_20482048 = Jeux_2048( Jeux_2048panel)
Jeux_20482048.start()
