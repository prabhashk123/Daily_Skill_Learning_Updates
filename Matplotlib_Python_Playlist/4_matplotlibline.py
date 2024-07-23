# linestyle or ls - it is used to change the style of the ploted line
import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([3,8,1,10])
# plt.plot(ypoint,ls = '--')
# plt.show()

## line color -(c)
import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([3,8,1,10])
# plt.plot(ypoint,ls = '--',color='r')
# # plt.plot(ypoint,ls = '--',c='r',marker='o',mec='y',mfc='k',ms=20)
# plt.show()

## Line width -(lw) .. width of line
import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([3,8,1,10])
# plt.plot(ypoint, linewidth='10')
# plt.show()

## Example for Multipleline
import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([3,8,1,10])
ypoint = np.array([6,2,7,11])
plt.plot(xpoint)
plt.plot(ypoint)
# plt.plot(xpoint,ypoint)
plt.show()