import numpy as np
random=np.random.default_rng()
print(random.integers(6))
print(random.uniform(low=10,high=90,size=1))
laptops=np.array(['Dell','Hp','Lenovo','Asus'])
laptop=random.shuffle(laptops)
print(laptops)
print(laptop)