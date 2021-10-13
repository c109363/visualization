import matplotlib
import matplotlib.pyplot as plt
import pandas as pd             
import numpy as np
import os

colormap = 'jet'
units = ['T', 'RA', 'LA', 'RL', 'LL']
sensortypes = ['acc', 'gyro', 'mag']

window_size = 25 
overlap = 0.5
step_size = int(np.ceil(overlap * window_size))  
time = [i for i in range(0,window_size)] 
 
norm_max = [120.54, 28.46, 4.05] 
norm_min = [0, 0, 0]

t = np.sin(3.14159/3)
co = ['Oranges_r', 'RdPu_r', 'PuRd_r', 'GnBu_r','PuBu_r']     
def savefile(graphType):    
    temp, _ = filename.split('.')
    temp = temp.split('_')           
    dir1 = temp[0] 
    dir2 = temp[1] 
    sensorName =  sensortype
    prefix = os.path.join(graphType,dir2,dir1,segName) 
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    savesensorName = dir1 + '_' + sensorName +'_'+ dir2 + '_' + segName
    name = prefix + '/' + savesensorName+'.jpg'    
    plt.savefig(name, bbox_inches='tight', pad_inches = 0)

    


def AtoX(v): #tranform sensor data to displacement
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
        for j in range(0,window_size-1):
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
p = 20 
positonx = [0,p,-p,p,-p]
positonz = [0,p,p,-p,-p]   
lim = 30
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
    #head 
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
    
   


for filename0 in os.listdir(datafolder):#17 activitie file
    print('-----------------',filename0, 'start --------------------')
    for filename in os.listdir(datafolder + '/' + filename0):
        print(filename)       
        data = pd.read_csv(os.path.join(datafolder, filename0, filename)).values
        datalen = [row[0] for row in data]  
        subwindow_Num = len(datalen)//(window_size - step_size)
        
        for i in range(0,subwindow_Num-2):
            segName = 'segment'+str(i)
            seg_data = data[i*(window_size - step_size):(i+1)*window_size - step_size*i]

            for i in range(0,3):#3 type sensors                    
                sensortype = sensortypes[i]
                n_max = norm_max[i]
                n_min = norm_min[i] 
                
                x = []
                y = []
                z = []
                for j in range(0,5):#5units
                    unit = units[j]
                    u = 9*j
                    px = positonx[j]
                    pz = positonz[j]
                  
                    a = [row[u+3*i] for row in seg_data]
                    b = [row[u+3*i+1] for row in seg_data]
                    c = [row[u+3*i+2] for row in seg_data]                    
                    a = [(x - n_min)/(n_max - n_min) for x in a]
                    b = [(x - n_min)/(n_max - n_min) for x in b]
                    c = [(x - n_min)/(n_max - n_min) for x in c]                                     
                    a = AtoX(a)
                    b = AtoX(b)
                    c = AtoX(c)                 
                    x.append(a)
                    y.append(b)
                    z.append(c)      
                sensor(x,y,z)     
                people(x,y,z)
                plt.close("all")
                    
    print('-----------------',filename0, 'finish --------------------')