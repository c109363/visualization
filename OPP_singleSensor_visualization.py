import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt           
import numpy as np
import os
from pyts.image import GramianAngularField
sensor = ['RKN^', 'HIP', 'LUA^', 
          'RUA_', 'LH', 'BACK', 
          'RKN_', 'RWR', 'RUA^', 
          'LUA_', 'LWR', 'RH']

window_size = 30 # sliding window size 1000ms
overlap = 0.5 # overlap 500ms
step_size = int(np.ceil(overlap * window_size))   
norm_max = 3000 
norm_min = 0
t = np.sin(3.14159/3)
colormap = 'jet'

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
    dir3 = temp[3] + '_' + temp[4]  # dir3 - people+run - S1A1     
    prefix = os.path.join(graphType, dir1, dir2, dir3, segName)    
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    savesensorName = sensorname +'_'+ dir1 +'_'+ dir3 +'_'+ segName
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
    

def polar1(a, b, c, time): #poly line polar graph
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

    
        
def polar2(a, b, c, time):
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
    graphType = 'triangle_scatter_front'  
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
    

def circle1(a, b, c, time): # sensor value - axes position time - color
    graphType = 'circle1'
    position = [0*np.pi, -2/3*np.pi,-4/3*np.pi,-2*np.pi]
    point = np.dstack((a,b,c,a))    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,len(point[0])))
    for i in range(0,len(point[0])):
        ax.plot(position, point[0][i], color = col[i],linewidth=0.4)
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)            
    plt.ylim(-1, 1)
    plt.axis('off')    
    savefile(graphType)


def circle2(a, b, c, time): # sensorvalue - position  time - color
    graphType = 'circle2'    
    aline = np.arange(0*np.pi, -2/3*np.pi, -2/300*np.pi)
    bline = np.arange(-2/3*np.pi, -4/3*np.pi, -2/300*np.pi)
    cline = np.arange(-4/3*np.pi, -2*np.pi, -2/300*np.pi)    
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,len(a)))
    for i in range(0,len(a)):      
        ra = np.array([a[i]]*len(aline))
        rb = np.array([b[i]]*len(bline))
        rc = np.array([c[i]]*len(cline))       
        ax.plot(aline, ra, color = col[i], linewidth=0.4)
        ax.plot(bline, rb, color = col[i], linewidth=0.4)
        ax.plot(cline, rc, color = col[i], linewidth=0.4)   
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    ax.bar(2*np.pi, -1, 2*np.pi, color="grey",alpha=0.1)           
    plt.ylim(-1, 1)
    plt.axis('off')  
    savefile(graphType)
    plt.clf()
    

def circle3(a, b, c, time): # time - position sensor value - color
    graphType = 'circle3'    
    a = [(x+1)/2 for x in a] # map sensor value to (0,1) to map color
    b = [(x+1)/2 for x in b]
    c = [(x+1)/2 for x in c]    
    aline = np.arange(0*np.pi, -2/3*np.pi, -2/300*np.pi)
    bline = np.arange(-2/3*np.pi,-4/3*np.pi, -2/300*np.pi)
    cline = np.arange(-4/3*np.pi,-2*np.pi, -2/300*np.pi)       
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300    
    ax = plt.subplot(111,projection='polar')
    ax.set_theta_zero_location("N", 120.0)        
    colors = matplotlib.cm.get_cmap(colormap)
    for i in range(0,len(a)): 
        n = len(a)-i
        ra = np.array([n]*len(aline))
        rb = np.array([n]*len(aline))
        rc = np.array([n]*len(aline))       
        ax.stackplot(aline, ra, color = colors(a[i]))
        ax.stackplot(bline, rb, color = colors(b[i]))
        ax.stackplot(cline, rc, color = colors(c[i]))    
    ax.bar(2*np.pi, len(a)+1, 2*np.pi, color="grey",alpha=0.1)        
    plt.ylim(0, len(a))
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
    col = colors(np.linspace(0,1,len(time)))
    for i in range(0,len(time)-1):        
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
    col = colors(np.linspace(0,1,len(time)))
    for i in range(0,len(time)-1):        
        px = [x[i], x[i+1]]
        py = [y[i], y[i+1]]        
        plt.plot(px, py, color = col[i],linewidth=0.8)
    plt.ylim(0, 4/3) # zoom in y axe
    plt.xlim(1/3, 5/3) # zoom in x axe
    plt.axis('off')
    savefile(graphType)    
    
def triangle_X_Y_view(a,b,c,time):
    graphType = 'triangle_X_Y_view'  
    y = [(a - b + 2) * t / 3 for a,b in zip(a, b)]
    x = [(0.5 * a + 0.5 * b - c + 3)/3 for a,b,c in zip(a, b, c)]
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['figure.dpi'] = 300    
    bx = [0,0,len(time),len(time)]
    by = [0, 5/3, 5/3, 0] 
    plt.stackplot(bx,by, colors = "#EFEFEF", alpha=1)   
    
    colors = matplotlib.cm.get_cmap(colormap)
    col = colors(np.linspace(0,1,len(time)))
    for i in range(0,len(time)-1):        
        px = [time[i], time[i+1]]
        py = [y[i], y[i+1]]        
        qy = [x[i], x[i+1]]    
        plt.plot(px, py, color = col[i],linewidth=0.8)
        plt.plot(px, qy, color = col[i],linewidth=0.8)       
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
    col = colors(np.linspace(0,1,len(time)))
    zmin = np.min(c)-0.1
    xmax = np.max(b)
    d = zmin - xmax
    for i in range(0,len(time)-1):        
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

def gaf(a,b,c):
    graphType = 'gaf'
    a = np.expand_dims(a, axis=0)
    b = np.expand_dims(b, axis=0)
    c = np.expand_dims(c, axis=0)  
    gadf = GramianAngularField(image_size=window_size, method='difference')    
    a_gadf = gadf.fit_transform(a)
    b_gadf = gadf.fit_transform(b)
    c_gadf = gadf.fit_transform(c)    
    img = np.concatenate([a_gadf, b_gadf, c_gadf], axis=0)
    img = np.swapaxes(img,0,2)     
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300
    plt.imshow(img, cmap = colormap, origin='lower')  # cmap = colormap,
    plt.axis('off')    
    savefile(graphType)

def val(x):
    for i in range(0,len(x)):
        
        if x[i] > 1:
            x[i] = 1
        if x[i] < 0:
            x[i] = 0
    return x
    
def polarColor(a, b, c, time): 
    graphType = 'color_rgb_polar'   
    a = [(x+1)/2 for x in a]
    b = [(x+1)/2 for x in b]
    c = [(x+1)/2 for x in c]
    a = val(a)
    b = val(b)
    c = val(c)
    time_r = [2 * np.pi * x /(window_size-1) for x in time]   
    plt.figure(figsize=(1,1))
    matplotlib.rcParams['savefig.dpi'] = 300   
    ax = plt.subplot(111,projection='polar')    
    q = np.dstack((a,b,c))
    q = q[0]   
    y = np.array([0.6]*len(time_r))   
    ax.scatter(time_r, y, facecolor = q, edgecolors='none',s=160)   
    ax.bar(2*np.pi, 1, 2*np.pi, color="grey",alpha=0.1)
    plt.ylim(0, 1)
    plt.axis('off')    
    savefile(graphType)   

def colorbox(a,b,c,time):
    graphType = 'color_rgb_square'
    a = [(x+1)/2 for x in a]
    b = [(x+1)/2 for x in b]
    c = [(x+1)/2 for x in c]
    a = val(a)
    b = val(b)
    c = val(c)    
    y = np.array([1]*len(time)) 
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

for filename0 in os.listdir('processedData'):#read 17 activitie file
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
            for i in range(0,12):
                sensorname = sensor[i]          
                num = i*3 + 1
                ''' a - sensor X   b - sensor Y  c - sensor Z'''                       
                a = [row[num] for row in seg_data]
                b = [row[num + 1] for row in seg_data]
                c = [row[num + 2] for row in seg_data]
                a = [(x - norm_min)/(norm_max - norm_min) for x in a]
                b = [(x - norm_min)/(norm_max - norm_min) for x in b]
                c = [(x - norm_min)/(norm_max - norm_min) for x in c]
                time = [i for i in range(0,len(a))] 
                line(a,b,c,time)

                circle1(a, b, c, time)
                circle2(a, b, c, time)
                circle3(a, b, c, time)
                polar1(a, b, c, time)
                polar2(a, b, c, time)

                triangle_origin_line(a,b,c,time)
                triangle_zoomin_line(a,b,c,time)
                triangle_X_Y_view(a,b,c,time)
                threeD(a,b,c,time)
                triangle_zoomin_scatter(a,b,c,time)
                gaf(a,b,c)
                polarColor(a, b, c, time)
                colorbox(a,b,c,time)
                plt.close("all")
                
    print('-----------------',filename0, 'finish --------------------')
            
            
        
        
        
        
        
        
        

    
    
    

