import matplotlib
import matplotlib.pyplot as plt
import pandas as pd             
import numpy as np
import os

sensor = ['RKN^', 'HIP', 'LUA^', 
          'RUA_', 'LH', 'BACK', 
          'RKN_', 'RWR', 'RUA^', 
          'LUA_', 'LWR', 'RH']
window_size = 30
overlap = 0.5
step_size = int(np.ceil(overlap * window_size))   
norm_max = 3000 
norm_min = 0
t = np.sin(3.14159/3)
colormap = 'jet'
time = [i for i in range(0,window_size)] 
co = ['Oranges_r', 'RdPu_r', 'PuRd_r', 'GnBu_r','PuBu_r']   

def savefile(graphType):    
    temp, _ = filename.split('.')
    temp = temp.split('_')            
    dir1 = temp[0] + '_' + temp[1] + '_' + temp[2]  
    if temp[3][:2] == 'S1': # dir2 - people 
        dir2 = 'people_01'
    elif temp[3][:2] == 'S2':
        dir2 = 'people_02'
    elif temp[3][:2] == 'S3':
        dir2 = 'people_03'
    else:
        dir2 = 'people_04'
    dir3 = temp[3] + '_' + temp[4]   
    prefix = os.path.join(graphType, dir1, temp[3])    
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    savesensorName = dir1 +'_'+ dir3 +'_'+ segName
    name = prefix + '/' + savesensorName+'.jpg'    
    plt.savefig(name, bbox_inches='tight', pad_inches = 0)
    
def AtoX(v):
    temp1 = 0
    temp2 = 0
    vv = [0 for _ in range(window_size)]
    for i in range(0,window_size):
        v[i] = v[i] + temp1
        temp1 = v[i]
        vv[i] = v[i]
        v[i] = vv[i] + temp2
        temp2 = v[i]  
    return v 

def sensor(x,y,z):
    graphType = '3DtraceSensorX'  
    fig = plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300
    ax = fig.gca(projection='3d')
    for i in range(0,len(x)):
        colormap = co[i]      
        colors = matplotlib.cm.get_cmap(colormap)
        col = colors(np.linspace(0,1,window_size))
        for j in range(0,window_size-2):
            a = [x[i][j], x[i][j+1]]
            b = [y[i][j], y[i][j+1]]
            c = [z[i][j], z[i][j+1]]
            ax.plot(a, b, c, color = col[j],linewidth=2,alpha = 0.3)

    ax.set_xlim3d(-lim, lim)
    ax.set_ylim3d(-lim, lim)
    ax.set_zlim3d(-lim, lim)
    plt.axis('off') 
       
    savefile(graphType)
    plt.show() 
p = 40 
positonx = [0,p,-p,p,-p]
positonz = [0,p,p,-p,-p]   
lim = 70
datafolder = 'data'
l = 2
ss = 10

def people(x,y,z):
    graphType = '3DtracePeopleX'  
    fig = plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300
    ax = fig.gca(projection='3d')
   
    colormap = 'jet'     
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
        
    cm=plt.cm.get_cmap('jet')    
    #tore
    tx,ty,tz = x[0],y[0],z[0]
  
    #RA
    rax,ray,raz = x[1],y[1],z[1]
    rax = [x+p for x in rax]
    raz = [x-p for x in raz]    
    #lA
    lax,lay,laz = x[2],y[2],z[2]
    lax = [x-p for x in lax]
    laz = [x-p for x in laz]
    #RL
    rlx,rly,rlz = x[3],y[3],z[3]
    rlx = [x+p for x in rlx]
    rlz = [x-2*p for x in rlz]
    #LL
    llx,lly,llz = x[4],y[4],z[4]
    llx = [x-p for x in llx]
    llz = [x-2*p for x in llz]
    #-----------position    
    #head tx ty tz+p
    hz = [x+p for x in tz]
    ax.scatter(tx,ty,hz, c=time, cmap=cm, edgecolors='none',s=100,alpha = 0.1)
    ttz = [x-p for x in tz]
    #body
    for i in range(0,window_size):
            a1 = [tx[i],tx[i]]
            b1 = [ty[i], ty[i]]
            c1 = [hz[i], ttz[i]]    
            ax.plot(a1, b1, c1, color = col[i],linewidth=l,alpha = 0.1)
            
            a2 = [tx[i], rax[i]]
            b2 = [ty[i], ray[i]]
            c2 = [tz[i], raz[i]]    
            ax.plot(a2, b2, c2, color = col[i],linewidth=l,alpha = 0.1)
            
            a3 = [tx[i], lax[i]]
            b3 = [ty[i], lay[i]]
            c3 = [tz[i], laz[i]]    
            ax.plot(a3, b3, c3, color = col[i],linewidth=l,alpha = 0.1)
            
            a4 = [tx[i],rlx[i]]
            b4 = [ty[i], rly[i]]
            c4 = [ttz[i], rlz[i]]    
            ax.plot(a4, b4, c4, color = col[i],linewidth=l,alpha = 0.1)
            
            a5 = [tx[i],llx[i]]
            b5 = [ty[i], lly[i]]
            c5 = [ttz[i], llz[i]]    
            ax.plot(a5, b5, c5, color = col[i],linewidth=l,alpha = 0.1)
    #T
    ax.scatter(tx,ty,tz, c=time, cmap=cm, edgecolors='none',s=ss,alpha = 0.5)  
    ax.scatter(rax,ray,raz, c=time, cmap=cm, edgecolors='none',s=ss,alpha = 0.5) 
    ax.scatter(lax,lay,laz, c=time, cmap=cm, edgecolors='none',s=ss,alpha = 0.5) 
    ax.scatter(rlx,rly,rlz, c=time, cmap=cm, edgecolors='none',s=ss,alpha = 0.5) 
    ax.scatter(llx,lly,llz, c=time, cmap=cm, edgecolors='none',s=ss,alpha = 0.5) 
          
    ax.set_xlim3d(-2*lim, 2*lim)
    ax.set_ylim3d(-lim, lim)
    ax.set_zlim3d(-lim, lim)
    plt.axis('off') 
    savefile(graphType)
    plt.show()   


    
for filename0 in os.listdir('processedData'):#17 activitie file
    print('-----------------',filename0, 'start --------------------')

    for filename in os.listdir('processedData/'+filename0):
        print(filename)       
        data = pd.read_csv(os.path.join('processedData', filename0, filename)).values
        data = np.nan_to_num(data)
        datalen = [row[0] for row in data]  
        
        subwindow_Num = len(datalen)//(window_size - step_size)
        for i in range(0,subwindow_Num-2):
            segName = 'segment'+str(i)
            seg_data = data[i*(window_size - step_size):(i+1)*window_size - step_size*i]
           
            ''' read 12 sensors data'''
            x = []
            y = []
            z = []
            for i in range(0,12):     
                num = i*3 + 1
                ''' a - sensor X   b - sensor Y  c - sensor Z'''                       
                a = [row[num] for row in seg_data]
                b = [row[num + 1] for row in seg_data]
                c = [row[num + 2] for row in seg_data]
                a = [(x - norm_min)/(norm_max - norm_min) for x in a]
                b = [(x - norm_min)/(norm_max - norm_min) for x in b]
                c = [(x - norm_min)/(norm_max - norm_min) for x in c]
                a = AtoX(a)
                b = AtoX(b)
                c = AtoX(c)
                x.append(a)
                y.append(b)
                z.append(c) 
            x = [x[5],x[8],x[3],x[2],x[9]]
            y = [y[5],y[8],y[3],y[2],y[9]]
            z = [z[5],z[8],z[3],z[2],z[9]]
            sensor(x,y,z)     
            people(x,y,z)
            plt.close("all")
                
    print('-----------------',filename0, 'finish --------------------')