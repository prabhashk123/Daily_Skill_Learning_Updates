# Now in this section we will create Bars bar()
# Vertical Bar
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.show()

# Horigental Bar
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y)
plt.show()

# Color of the bar() and barh()
# By default Vertical Bar
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color='r')
plt.show()

# How we can change the bar width by default vertical bar

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width=0.3)
plt.show()

# for Horizental bar you have to use height insted of width
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height=0.3)
plt.show()

"""Notes:-(1)Horzental bar ki height by default(0.8) hoti hai.
(2)Vertical Bar ki width 0.5 ya 1 hoti hai.
"""