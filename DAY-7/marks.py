import numpy as np
marks=np.array([[90, 85, 60],
                [88, 92, 95]])
marks[(marks>50)&(marks<=70)]=4
print(marks)
#print("Comparison:")
print("Addition is: \n",marks+marks)
