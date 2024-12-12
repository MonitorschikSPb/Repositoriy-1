import numpy as np
import matplotlib.pyplot as plt
def f(x, alpha, betta):
return (xbetta + alphabetta) / x**betta

x = np.linspace(1, 10, 100)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(x, f(x, alpha=1, betta=1), label='alpha=1, betta=1')
plt.title('alpha=1, betta=1')

plt.subplot(1, 3, 2)
plt.plot(x, f(x, alpha=2, betta=1), label='alpha=2, betta=1')
plt.title('alpha=2, betta=1')

plt.subplot(1, 3, 3)
plt.plot(x, f(x, alpha=1, betta=2), label='alpha=1, betta=2')
plt.title('alpha=1, betta=2')

plt.tight_layout()
plt.show()