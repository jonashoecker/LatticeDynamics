import matplotlib.pyplot as plt
import math as m

position_u = [0.5, 1.5, 2.5, 3.5]
position_v = [1, 2, 3]

def amplitude(k, j):
    return m.sin(k * j)

fig, axs = plt.subplots(4, 2, figsize=(9, 12))

for n in range(1, 5):
    k = n * m.pi / 4

    values_u_acoustic = [amplitude(k, pos) for pos in position_u]
    values_v_acoustic = [amplitude(k, pos) for pos in position_v]
    values_u_optical = [amplitude(k, pos) for pos in position_u]
    values_v_optical = [-amplitude(k, pos) for pos in position_v]

    axs[n - 1, 0].plot(position_u, values_u_acoustic, marker='o', color='red', linestyle='', label="Mass mu (Acoustic)")
    axs[n - 1, 0].plot(position_v, values_v_acoustic, marker='o', color='green', linestyle='', label="Mass mv (Acoustic)")
    for x, y in zip(position_u, values_u_acoustic):
        axs[n - 1, 0].plot([x, x], [0, y], linestyle='dotted', color='red')
    for x, y in zip(position_v, values_v_acoustic):
        axs[n - 1, 0].plot([x, x], [0, y], linestyle='dotted', color='green')
    axs[n - 1, 0].set_title("Acoustic Mode (n={})".format(n), fontsize=14)
    axs[n - 1, 0].grid(True)
    axs[n - 1, 0].set_ylim(-1.5, 1.5)
    axs[n-1, 0].set_xticks([])
    axs[n-1, 0].set_yticks([])

    axs[n - 1, 1].plot(position_u, values_u_optical, marker='o', color='red', linestyle='', label="Mass mu (Optical)")
    axs[n - 1, 1].plot(position_v, values_v_optical, marker='o', color='green', linestyle='', label="Mass mv (Optical)")
    for x, y in zip(position_u, values_u_optical):
        axs[n - 1, 1].plot([x, x], [0, y], linestyle='dotted', color='red')
    for x, y in zip(position_v, values_v_optical):
        axs[n - 1, 1].plot([x, x], [0, y], linestyle='dotted', color='green')
    axs[n - 1, 1].set_title("Optical Mode (n={})".format(n), fontsize=14)
    axs[n - 1, 1].grid(True)
    axs[n - 1, 1].set_ylim(-1.5, 1.5)
    axs[n-1, 1].set_xticks([])
    axs[n-1, 1].set_yticks([])

plt.tight_layout()
plt.show()
