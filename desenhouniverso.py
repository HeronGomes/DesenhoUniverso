# -*- coding: utf-8 -*-

import numpy as np

import cv2 as cv

imagem = np.full((1000,1000,3),(0,0,0),np.uint8)

qt_estrelas = np.random.randint(1e2,1e3)

filme = cv.VideoWriter('./universo.mp4',cv.VideoWriter.fourcc(*'mp4v'),15,(1000,1000))

def desenha_sol(tamanho):
       
    cv.circle(imagem,
              (500,500),
              tamanho,
              (0,255,255),
              cv.FILLED,
              cv.LINE_AA)
    cv.imshow('Universo',imagem)
    filme.write(imagem)
    cv.waitKey(20)

def desenha_planeta(frame):
        
  
    posicao = 0.0
    
    while True:
        
        imagem_planeta = frame.copy()
        
        #Planeta gigante esquerda superior
        
        x = int(1300)
        y = int(1)
        
        cv.circle(imagem_planeta,
                  (x,y),
                  600,
                  (255,255,224),
                  cv.FILLED,
                  cv.LINE_AA)
                
        
        #Aneis do planeta gigante
        
        for anel in range(0,150,20):
        
            cv.ellipse(imagem_planeta,
                       (1200-anel,1+anel),
                       (250,800),
                       (30),
                       (0),
                       (360),
                       (255,64,64),
                       8,
                       cv.LINE_AA
                       )
        
        
        #Ordem Solar
        

    
        x = int(500 + 100 * np.cos(posicao))
        y = int(500 + 100 * np.sin(posicao))
        
        cv.circle(imagem_planeta,
                 (x,y),
                 8,
                 (0,0,255),
                 cv.FILLED,
                 cv.LINE_AA)
        
        x = int(500 + 200 * np.cos(posicao+5))
        y = int(500 + 200 * np.sin(posicao+5))
        
        cv.circle(imagem_planeta,
                 (x,y),
                 16,
                 (0,255,0),
                 cv.FILLED,
                 cv.LINE_AA)
    
    
    
        x = int(500+300 * np.cos(posicao-15))
        y = int(500+300 * np.sin(posicao-15))
        
        cv.circle(imagem_planeta,
                  (x,y),
                  20,
                  (255,0,0),
                  cv.FILLED,
                  cv.LINE_AA)
    
        x = int(500+300 * np.cos(posicao-50))
        y = int(500+300 * np.sin(posicao-50))
        
        cv.circle(imagem_planeta,
                  (x,y),
                  24,
                  (255,0,255),
                  cv.FILLED,
                  cv.LINE_AA)
    
    
    
        #Planeta com lua
        
        x = int(500+450 * np.cos(posicao))
        y = int(500+450 * np.sin(posicao))
        
        cv.circle(imagem_planeta,
                  (x,y),
                  28,
                  (127,127,127),
                  cv.FILLED,
                  cv.LINE_AA)
        
        #Luas do planeta
    
        xi = int(x+50* np.cos(posicao*2))
        yi = int(y+50* np.sin(posicao*2))
        
        cv.circle(imagem_planeta,
                  (xi,yi),
                  8,
                  (127,0,127),
                  cv.FILLED,
                  cv.LINE_AA)
        
        
        xi = int(x+100* np.cos(posicao*3))
        yi = int(y+100* np.sin(posicao*3))
        
        cv.circle(imagem_planeta,
                  (xi,yi),
                  8,
                  (0,0,127),
                  cv.FILLED,
                  cv.LINE_AA)
        
        #Planeta com orbita zuada
    
        x = int(250*np.cos(posicao+1))
        y = int(500*np.sin(posicao)*2)
        
        cv.circle(imagem_planeta,
                  (x,y),
                  32,
                  (127,0,64),
                  cv.FILLED,
                  cv.LINE_AA)
        
        
        #Buraco negro
        
        x = int(200+50*np.cos(posicao))
        y = int(50)
        
        for horizonte_eventos in range(0,10,2):
        
            cv.ellipse(imagem_planeta,
                           (x+horizonte_eventos,y+horizonte_eventos),
                           (60,5),
                           (180),
                           (0),
                           (360),
                           (127,127,240),
                           1,
                           cv.LINE_AA
                           )
            
            cv.circle(imagem_planeta,
                      (x,y),
                      16+horizonte_eventos,
                      (210,210,240),
                      1,
                      cv.LINE_AA)
    
        posicao += 0.1
        
        cv.imshow('Universo',imagem_planeta)
        filme.write(imagem_planeta)
        tecla = cv.waitKey(50)
        
        if tecla == ord('q'):
            break

def desenha_estrelas():
    
    x = np.random.randint(1,999)
    
    y = np.random.randint(1,999)
    
    cv.circle(imagem,
              (x,y),
              np.random.randint(0,5),
              (255,255,255),
              cv.FILLED)

    cv.imshow('Universo',imagem)
    filme.write(imagem)
    cv.waitKey(5)
    
    
for qt in range(qt_estrelas):
    desenha_estrelas()
    
    
    
for tamanho_sol in range(100):
    desenha_sol(tamanho_sol)


desenha_planeta(imagem)
    
filme.release()
cv.waitKey()
cv.destroyAllWindows()
