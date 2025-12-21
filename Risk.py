from random import randint
def tamado_jatekos():
    
    dobasok1=[randint(1,6) for i in range(3)]  
    return dobasok1

    

tamado_jatekos()
def vedekezo_jatekos():
    
    dobasok2=[randint(1,6) for j in range(2)]
    return dobasok2

vedekezo_jatekos()
attack=0
dontetlen=0
defender=0
import math
#def prob_vedor():
 #   osszeg=0
   # for i in range(1,7):
      #  for j in range(1,i):
       #    for k in range(3,j+2):
          #     osszeg=+(math.comb(k,3)+math.comb(k-1,2))
       # osszeg=+math.comb(i,3)
   # print(osszeg)
#prob_vedor()
def prob():
    vedol=[]
    tamadol=[]
    vedop=[]
    tamadop=[]
    dontetlen=[]
    q=[]

    
    for i in range(1,7):
        
        for j in range(1,7):
            rendezetlenv=[i,j]
            rendezetlenv.sort()
            vedol.append(rendezetlenv)
    #print(vedol,len(vedol))
    for i in range(1,7):
        
        for j in range(1,7):
            for k in range(1,7):
                rendezetlent=[i,j,k]
                rendezetlent.sort()
                tamadol.append(rendezetlent)
    #print(tamadol,len(tamadol))
    for k in (range(1)):
        for i in range(len(vedol)):
            
            for j in range(len(tamadol)):
               if vedol[i][-1]>=tamadol[j][-1] and vedol[i][-2]>=tamadol[j][-2]:
                   #vedop.append(vedol[i])
                   #vedop.append(tamadol[j])
                   vedop.append(1)
               elif vedol[i][-1]<tamadol[j][-1] and vedol[i][-2]<tamadol[j][-2]:
                   tamadop.append(1)
                   #tamadop.append(vedol[i])
                   #tamadop.append(tamadol[j])
               
               elif (vedol[i][-1]>=tamadol[j][-1] and vedol[i][-2]>=tamadol[j][-2])==False or (vedol[i][-1]<tamadol[j][-1] and vedol[i][-2]<tamadol[j][-2])==False:
                   dontetlen.append(1)
                   #dontetlen.append(vedol[i])
                   #dontetlen.append(tamadol[j])
               else:
                   q.append([i])
                   q.append([j])
    #vedol[i][-1]<tamadol[j][-1] and vedol[i][-2]>=tamadol[j][-2]) or  (vedol[i][-1]>=tamadol[j][-1] and vedol[i][-2]<tamadol[j][-2]):
    osszes_eset=len(vedol)*len(tamadol)
    p_vedo=len(vedop)/osszes_eset
    p_tamado=len(tamadop)/osszes_eset
    p_dontetlen=len(dontetlen)/osszes_eset
    #print(len(vedol),len(tamadol))
    #(f"{'1000000 kísérlet:'}   {yattack_valseg:.5f}   {ydontetlen_valseg:.5f}   {ydefender_valseg:.5f}")
    return (f"{'Valószínűség:':<12}{p_tamado:>14.5f}   {p_dontetlen:.5f}   {p_vedo:.5f}")  
    #print(len(vedop), len(tamadop), len(dontetlen), len(vedop)+len(tamadop)+len(dontetlen))
    #print(dontetlen)
    
prob()


               
#def counting(attack, dontetlen, defender):
 #   attack=+attack
 #   dontetlen=+dontetlen
  ##  defender=+defender
    #return(attack,dontetlen,defender)
#counting(1,0,0)


def fight_func(x,y):
    p=(prob())
    for i in range(1):
        attack=[]
        defender=[]
        dontetlen=[]
        s=0
    
        for i in range(x):
            tamado=0
            vedo=0
            #attack=[]
            #defender=[]
            #dontetlen=[]
            t=tamado_jatekos()
            t1=t.copy()
            lista=[]
            v=vedekezo_jatekos()
            v1=v.copy()
            t.sort()
            v.sort()
            if t[2]>v[1]:
                tamado=+1
            
            if t[2]<=v[1]:
                vedo=+1
            if t[1]>v[0]:
                tamado=+1
            if t[1]<=v[0]:
                vedo=+1
            #print(t,v)
            #print(tamado,vedo)
            
        
            if tamado==1 and vedo==0:
                attack.append(s)
            if vedo==1 and tamado==0:
                defender.append(s)
            if vedo==1 and tamado==1:
                dontetlen.append(s)
            attack_valseg=(len(attack)/x)
            dontetlen_valseg=(len(dontetlen)/x)
            defender_valseg=(len(defender)/x)
    #print(len(attack), attack_valseg, len(dontetlen), len(defender))
    for i in range(1):
        attack=[]
        defender=[]
        dontetlen=[]
        s=0
    
        for i in range(y):
            tamado=0
            vedo=0
            #attack=[]
            #defender=[]
            #dontetlen=[]
            t=tamado_jatekos()
            t1=t.copy()
            lista=[]
            v=vedekezo_jatekos()
            v1=v.copy()
            t.sort()
            v.sort()
            if t[2]>v[1]:
                tamado=+1
            
            if t[2]<=v[1]:
                vedo=+1
            if t[1]>v[0]:
                tamado=+1
            if t[1]<=v[0]:
                vedo=+1
            #print(t,v)
            #print(tamado,vedo)
            
        
            if tamado==1 and vedo==0:
                attack.append(s)
            if vedo==1 and tamado==0:
                defender.append(s)
            if vedo==1 and tamado==1:
                dontetlen.append(s)
            yattack_valseg=(len(attack)/y)
            ydontetlen_valseg=(len(dontetlen)/y)
            ydefender_valseg=(len(defender)/y)
                
    #print(len(attack), len(dontetlen), len(defender))
    kis=(attack_valseg,dontetlen_valseg,defender_valseg)
    nagy=(yattack_valseg,ydontetlen_valseg,ydefender_valseg)
    osszes_eset=6**3*6**2
    
    
    
    print(f"{'':<16} {'Támadó':>9}    {'Döntetlen':>4}{'Védő':>5}")
    print(f"{'1000 kísérlet:':<12}      {attack_valseg:.5f}   {dontetlen_valseg:.5f}   {defender_valseg:.5f}")
    print(f"{'1000000 kísérlet:'}   {yattack_valseg:.5f}   {ydontetlen_valseg:.5f}   {ydefender_valseg:.5f}")
    
    print(prob())

   
fight_func(1000,1000000)       
if __name__=="__fight_func__":
    fight_func(1000,1000000)
