from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
import sys

import os

path = "/home/harley/Imagens/testes/4"

seq=os.listdir(path)


# this lists all the file
count =0
for i,rem in enumerate(seq):
    extension =  rem.split(".")[-1]
    name = rem;
    filename = path + '/' + rem
    rem = open(path + '/' + rem, "r")
    translacoes = [100, 100]
    escalas   = [0.5, 2]
    rotacoes  = [90,  180, 270, 360]
     
    with Image(filename=filename) as img:
        with img.clone() as i:
            for escala in escalas :
                for rotacao in rotacoes:       
                   i.rotate(rotacao)  
                   i.transform('500x500', '100%')  
                         
                   tmpfile =  path + "/" + "test_"+ str(rotacao) + "_"+ str(escala) + name 
                   i.save(filename=tmpfile)
                    

