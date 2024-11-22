import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = -1.5 * x + 3

fig, ax = plt.subplots()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.plot(x, y, linewidth=2)
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)
ax.set_xticks([i for i in np.arange(-4, 10) if i != 0])
ax.set_xticks([i for i in np.arange(-3.5, 9)], minor=True)
ax.set_yticks([i for i in np.arange(-4, 10) if i != 0])
ax.set_yticks([i for i in np.arange(-3.5, 9)], minor=True)
ax.tick_params(which="both", direction="inout")
for i in ax.get_xticks():
    ax.axvline(i, color="lightgray", linewidth=0.5, zorder=-10)
for i in ax.get_yticks():
    ax.axhline(i, color="lightgray", linewidth=0.5, zorder=-10)
for i in ax.get_xticks(minor=True):
    ax.axvline(i, color="lightgray", linewidth=0.5, linestyle=":", zorder=-10)
for i in ax.get_yticks(minor=True):
    ax.axhline(i, color="lightgray", linewidth=0.5, linestyle=":", zorder=-10)
ax.set_aspect("equal")

plt.show()
