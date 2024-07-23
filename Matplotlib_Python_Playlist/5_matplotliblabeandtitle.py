# Create labels for plot:-
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,290,300,310,320,325,330])
plt.plot(x,y)
plt.xlabel("Average oxygen",c='r')
plt.ylabel("Our calorie",c='r')
plt.show()

## Create Tiltle for plot:-
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,290,300,310,320,325,330])
# plt.plot(x,y,c='g',lw='10',marker='o',ms='10',mec='k',mfc='b')
# plt.title("Health Monitor",c='y')
# plt.xlabel("Average oxygen",c='r')
# plt.ylabel("Our calorie",c='r')
# plt.show()

## Now we will set the font property for title and labels 
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,290,300,310,320,325,330])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

# plt.plot(x,y)
# plt.title("Health Monitor",fontdict=font1)
# plt.xlabel("Average oxygen",fontdict=font2)
# plt.ylabel("Our calorie",fontdict=font2)
# plt.show()

## You can also change the location of title via "loc":-
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,290,300,310,320,325,330])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.plot(x,y)
plt.title("Health Monitor",fontdict=font1,loc='left')
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("Our calorie",fontdict=font2)
plt.show()