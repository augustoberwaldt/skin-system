from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
import sys

import os

path = "/home/harley/Imagens/doencas/pso"

seq=os.listdir(path)


# this lists all the file
count =0
for i,rem in enumerate(seq):
    extension =  rem.split(".")[-1]
    name = rem;
    filename = path + '/' + rem
    rem = open(path + '/' + rem, "r")
    translacoes = [-100, +100]
    escalas   = [0.5, 2]
    rotacoes  = [90,  180, 270, 360]
     
    with Image(filename=filename) as img:
       for rotacao in rotacoes :
            with img.clone() as i:
                i.rotate(rotacao)                       
             
                tmpfile =  path + "/" + "test_"+ str(rotacao)+ name 
                i.save(filename=tmpfile)
                    

