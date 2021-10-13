import matplotlib
import matplotlib.pyplot as plt
import pandas as pd             
import numpy as np
import os

colormap = 'jet'
units = ['T', 'RA', 'LA', 'RL', 'LL']
sensortypes = ['acc', 'gyro', 'mag']

window_size = 25 #sliding window 25hz - 1000ms
overlap = 0.5
step_size = int(np.ceil(overlap * window_size))  
time = [i for i in range(0,window_size)] 
 
norm_max = [120.54, 28.46, 4.05] #  maximum of absolute value
norm_min = [0, 0, 0]

t = np.sin(3.14159/3)
colormap = 'jet'
    
def savefile(graphType):    
    temp, _ = filename.split('.')
    temp = temp.split('_')           
    dir1 = temp[0] 
    dir2 = temp[1]  
    sensorName =  unit +'_'+ sensortype
    prefix = os.path.join(graphType, dir2, dir1, segName)
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    savesensorName = dir1 + '_' + sensorName +'_'+ dir2 + '_' + segName
    name = prefix + '/' + savesensorName+'.jpg'    
    plt.savefig(name, bbox_inches='tight', pad_inches = 0)
       
def line(a,b,c,time):
    graphType = 'line'   
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300   
    bx = [0,0,window_size,window_size]
    by = [0,1,1,0]
    by2 = [0,-1,-1,0]  
    plt.stackplot(bx,by, colors = "#EFEFEF", alpha=1) #line graph backgroud   
    plt.stackplot(bx,by2, colors = "#EFEFEF", alpha=1)
    plt.stackplot(time, a, colors = 'r', alpha=0.1) # fill style  
    plt.plot(time, a, color = 'r', linewidth=0.3)   # line style  
    plt.stackplot(time, b, colors = 'g', alpha=0.1)
    plt.plot(time, b, color = 'g', linewidth=0.3)  
    plt.stackplot(time, c, colors = 'b', alpha=0.1)
    plt.plot(time, c, color = 'b', linewidth=0.3)    
    plt.ylim(-1, 1)
    plt.xlim(0, window_size-1)
    plt.axis('off')   
    savefile(graphType)
    
    
def polar1(a, b, c, time): 
    graphType = 'polar1'   
    time_r = [2 * np.pi * x /(window_size-1) for x in time]    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')    
    ax.stackplot(time_r, c, colors = 'b', alpha=0.1)
    ax.plot(time_r, c, linewidth=0.3,color='b')           
    ax.stackplot(time_r, b, colors = 'g', alpha=0.1)
    ax.plot(time_r, b, linewidth=0.3,color='g')           
    ax.stackplot(time_r, a, colors = 'r', alpha=0.1)
    ax.plot(time_r, a, linewidth=0.3,color='r')           
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)            
    plt.ylim(-1, 1)
    plt.axis('off')    
    savefile(graphType)
        
def polar2(a, b, c, time):# three coordinate polar
    graphType = 'polar2'   
    time_r = [2 * np.pi * x /(window_size-1) for x in time]   
    b = [x+2 for x in b]
    c = [x+4 for x in c]   
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300   
    ax = plt.subplot(111,projection='polar')
    ax.plot(time_r, c, linewidth=0.3,color='b')
    ax.fill_between(time_r, 4, c,facecolor='b', alpha=0.1)
    ax.plot(time_r, b, linewidth=0.3,color='g')
    ax.fill_between(time_r, 2, b,facecolor='g', alpha=0.1)
    ax.plot(time_r, a, linewidth=0.3,color='r')
    ax.fill_between(time_r, 0, a,facecolor='r', alpha=0.1)           
    ax.bar(2*np.pi, 5, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)            
    plt.ylim(-1, 5)
    plt.axis('off')    
    savefile(graphType)
      
def triangle_origin_scatter(a,b,c,time):
    graphType = 'triangle_origin'  
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300  
    bx = [0,1,2]
    by = [0,2*t,0]
    plt.fill_between(bx, 0 , by, facecolor='#EFEFEF')
    cm=plt.cm.get_cmap(colormap)
    plt.scatter(x, y, c=time, cmap=cm, edgecolors='none',s=0.8)
    plt.ylim(0, 2)
    plt.xlim(0, 2)
    plt.axis('off')
    savefile(graphType)
    
def triangle_zoomin_scatter(a,b,c,time):
    graphType = 'triangle_zoomin'  
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300  
    bx = [2/3, 1/3, 2/3, 4/3, 5/3, 4/3] 
    by = [0, 2/3 * t, 4/3 * t, 4/3 * t, 2/3 * t, 0]
    plt.fill_between(bx, 0, by, facecolor='#EFEFEF')
    cm=plt.cm.get_cmap(colormap)
    plt.scatter(x, y, c=time, cmap=cm, edgecolors='none',s=0.8)
    plt.ylim(0, 4/3) # zoom in y axe
    plt.xlim(1/3, 5/3) # zoom in x axe
    plt.axis('off')
    savefile(graphType)    
    
def circle1(a, b, c, time):
    graphType = 'circle1'
    position = [0*np.pi, -2/3*np.pi,-4/3*np.pi,-2*np.pi]
    point = np.dstack((a,b,c,a))    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    for i in range(0,window_size):
        ax.plot(position, point[0][i], color = col[i],linewidth=0.4)
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)            
    plt.ylim(-1, 1)
    plt.axis('off')    
    savefile(graphType)


def circle2(a, b, c, time): 
    graphType = 'circle2'    
    aline = np.arange(0*np.pi, -2/3*np.pi, -1/300*np.pi)
    bline = np.arange(-2/3*np.pi, -4/3*np.pi, -1/300*np.pi)
    cline = np.arange(-4/3*np.pi, -2*np.pi, -1/300*np.pi)    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    for i in range(0,window_size):      
        ra = np.array([a[i]]*len(aline))
        rb = np.array([b[i]]*len(aline))
        rc = np.array([c[i]]*len(aline))       
        ax.plot(aline, ra, color = col[i], linewidth=0.4)
        ax.plot(bline, rb, color = col[i], linewidth=0.4)
        ax.plot(cline, rc, color = col[i], linewidth=0.4)   
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)           
    plt.ylim(-1, 1)
    plt.axis('off')  
    savefile(graphType)
    

def circle3(a, b, c, time): 
    graphType = 'circle3'    
    a = [(x+1)/2 for x in a] 
    b = [(x+1)/2 for x in b]
    c = [(x+1)/2 for x in c]    
    aline = np.arange(0*np.pi, -2/3*np.pi, -1/300*np.pi)
    bline = np.arange(-2/3*np.pi,-4/3*np.pi, -1/300*np.pi)
    cline = np.arange(-4/3*np.pi,-2*np.pi, -1/300*np.pi)       
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)        
    colors = matplotlib.cm.get_cmap(colormap)
    for i in range(0,window_size): 
        n = window_size-i
        ra = np.array([n]*len(aline))
        rb = np.array([n]*len(aline))
        rc = np.array([n]*len(aline))       
        ax.stackplot(aline, ra, color = colors(a[i]))
        ax.stackplot(bline, rb, color = colors(b[i]))
        ax.stackplot(cline, rc, color = colors(c[i]))    
    ax.bar(2*np.pi, window_size+1, 2*np.pi, color="grey",alpha=0.1)        
    plt.ylim(0, window_size)
    plt.axis('off')  
    savefile(graphType)    

    
def triangle_origin_line(a,b,c,time):#point
    graphType = 'triangle_origin_line'  
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300  
    bx = [0,1,2]
    by = [0,2*t,0]
    plt.fill_between(bx, 0 , by, facecolor='#EFEFEF')
    #cm=plt.cm.get_cmap(colormap)
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    for i in range(0,window_size-1):        
        px = [x[i], x[i+1]]
        py = [y[i], y[i+1]]        
        plt.plot(px, py, color = col[i],linewidth=0.8)
    plt.ylim(0, 2)
    plt.xlim(0, 2)
    plt.axis('off')
    savefile(graphType)
    
def triangle_zoomin_line(a,b,c,time):
    graphType = 'triangle_zoomin_line'  
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300  
    bx = [2/3, 1/3, 2/3, 4/3, 5/3, 4/3] 
    by = [0, 2/3 * t, 4/3 * t, 4/3 * t, 2/3 * t, 0]
    plt.fill_between(bx, 0, by, facecolor='#EFEFEF')
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    for i in range(0,window_size-1):        
        px = [x[i], x[i+1]]
        py = [y[i], y[i+1]]        
        plt.plot(px, py, color = col[i],linewidth=0.8)
    plt.ylim(0, 4/3) # zoom in y axe
    plt.xlim(1/3, 5/3) # zoom in x axe len
    plt.axis('off')
    savefile(graphType)    
    
def triangle_X_Y_view(a,b,c,time):
    graphType = 'triangle_X_Y_view'  
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300    
    bx = [0,0,window_size, window_size]
    by = [0, 5/3, 5/3, 0] 
    plt.stackplot(bx,by, colors = "#EFEFEF", alpha=1)   
    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    
    for i in range(0,window_size-1):        
        px = [i, i+1]
        py = [y[i], y[i+1]]        
        qy = [x[i], x[i+1]]    
        
        plt.plot(px, py, color = col[i], linewidth=0.8)
        plt.plot(px, qy, color = col[i], linewidth=0.8)       
    plt.ylim(0, 5/3) #0,4/3
    plt.xlim(0, window_size -1)
    plt.axis('off')
    savefile(graphType)
    
def threeD(a,b,c,time):#point
    graphType = '3D'  
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300  
    bx = [-1,-1,1,1]
    by = [-1,1,1,-1]
    plt.fill_between(bx, -1 , by, facecolor='#EFEFEF')
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,window_size))
    zmin = np.min(c)-0.1
    xmax = np.max(b)
    d = zmin - xmax
    for i in range(0,window_size-1):        
        x = [a[i], a[i+1]]
        y = [b[i], b[i+1]]
        z = [c[i], c[i+1]]
        y = [x + d for x in y]              
        plt.plot(x, y, color = '#959595',linewidth=0.8)
        plt.plot(x, z, color = col[i],linewidth=0.8)        
    plt.ylim(-1, 1)
    plt.xlim(-1, 1)
    plt.axis('off')
    savefile(graphType)
    

def colorpolar(a, b, c, time): #color
    a = [x*0.5+0.5 for x in a]
    b = [x*0.5+0.5 for x in b]
    c = [x*0.5+0.5 for x in c]
    graphType = 'color(polar)'   
    time_r = [2 * np.pi * x /(window_size-1) for x in time]   
    q = np.dstack((a,b,c))
    q = q[0]    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300      
    ax = plt.subplot(111,projection='polar')
    y = np.array([0.6] * window_size)   
    ax.scatter(time_r, y, facecolor = q, edgecolors='none',s=160)   
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    plt.ylim(0, 1)
    plt.axis('off')    
    savefile(graphType)   


def colorbox(a,b,c,time):
    a = [x*0.5+0.5 for x in a]
    b = [x*0.5+0.5 for x in b]
    c = [x*0.5+0.5 for x in c]
    graphType = 'colorbox'
    y = np.array([1]*window_size) 
    q = np.dstack((a,b,c))
    q = q[0] 
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    bx = [0,0,window_size,window_size]
    by = [0,1,1,0] 
    plt.stackplot(bx,by, colors = "#EFEFEF", alpha=1)
    plt.bar(time, y, width=1, color = q)
    plt.ylim(0, 1)
    plt.xlim(0, window_size-1)
    plt.axis('off')    
    savefile(graphType)
    
datafolder = 'data'

for filename0 in os.listdir(datafolder):#17 activitie file
    print('-----------------',filename0, 'start --------------------')
    for filename in os.listdir(datafolder + '/' + filename0):
        print(filename)       
        data = pd.read_csv(os.path.join(datafolder, filename0, filename)).values
        #data = np.nan_to_num(data)
        datalen = [row[0] for row in data]  
        subwindow_Num = len(datalen)//(window_size - step_size)
        
        for i in range(0,subwindow_Num-2):
            segName = 'segment'+str(i)
            seg_data = data[i*(window_size - step_size):(i+1)*window_size - step_size*i]
            
            for i in range(0,5):#5units
                unit = units[i]
                u = 9*i
                for i in range(0,3):#3 type sensors
                    sensortype = sensortypes[i]
                    n_max = norm_max[i]
                    n_min = norm_min[i]
                    
                    a = [row[u+3*i] for row in seg_data]
                    b = [row[u+3*i+1] for row in seg_data]
                    c = [row[u+3*i+2] for row in seg_data]
                    
                    a = [(x - n_min)/(n_max - n_min) for x in a]
                    b = [(x - n_min)/(n_max - n_min) for x in b]
                    c = [(x - n_min)/(n_max - n_min) for x in c]
                    
                    line(a,b,c,time)
                    
                    threeD(a,b,c,time)
                    triangle_zoomin_line(a,b,c,time)   
                    triangle_X_Y_view(a,b,c,time)
                    
                    polar1(a, b, c, time)                 
                    triangle_origin_line(a,b,c,time)                     
                    polar2(a, b, c, time)
                    colorbox(a,b,c,time)
                    colorpolar(a, b, c, time)                   
                    circle2(a, b, c, time)
                    circle3(a, b, c, time)
                    plt.cla()
                    plt.close("all")
                    
    print('-----------------',filename0, 'finish --------------------')
            
    
            
 
        
        
        

    
    
    

