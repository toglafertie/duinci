import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(1, 1.5, 1000)

# Create a seaborn joint plot with KDE
sns.jointplot(x=x, y=y, kind="kde", cmap="viridis")

plt.show()
