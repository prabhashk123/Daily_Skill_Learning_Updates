# markers means symbole as mark like point as a,b,c,d point show in graph
# you can use argument marker to emphasize each point with specified marker.anyting marker="string anything".

import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o')
# # plt.plot(ypoints,marker='*')
# plt.show()

# format strings 'fmt' means marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,'o:g')
# plt.show()
# here r is color and :colon means doted line

## line reference
# - solid line
# : doted line
# -- dashed line
# -. dashline/doted line

## Color reference
# r red
# g green
# b blue
# c cyan
# m magenta
# y yellow
# k black
# w white
# ya use #(hach) value if remember hai to.

## marker size-(ms)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms = 20)
# plt.show()

## marker edge color - (mec)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms = 20, mec='y')
# plt.show()

## marker face color - (mfc)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms = 20, mfc='y',mec='r')
plt.show()

