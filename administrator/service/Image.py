from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
import sys

import os
path = "/home/harley/Imagens/doencas/negativas"

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
    rotacoes  = [45, 90, 135, 180, 225, 270, 315]
     
    with Image(filename=filename) as img:
        with Drawing() as ctx:
            for rotacao in rotacoes:
                for escala in escalas:
                    for translacao in translacoes:  
                        with img.clone() as i:
                            
                            i.rotate(rotacao)
                            i.resize(int(i.width *  escala), int(i.height * escala))
                           
                            ctx.translate(translacao,translacao)
                            ctx(i)  
                            tmpfile =  path + "/" + str(rotacao) + "_" + str(escala) + "_" + str(count) +  "_" + name 
                            i.save(filename=tmpfile)
                        

    count = count + 1
