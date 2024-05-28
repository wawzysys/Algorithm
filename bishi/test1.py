import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_fixture():
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the base
    base = patches.Rectangle((2, 1), 6, 1, linewidth=1, edgecolor='black', facecolor='grey')
    ax.add_patch(base)
    ax.text(5, 1.2, 'Base', horizontalalignment='center')

    # Draw the flexible support arms with shock absorbers
    support_arm1 = patches.Rectangle((3, 2), 1, 4, linewidth=1, edgecolor='black', facecolor='lightgrey')
    support_arm2 = patches.Rectangle((6, 2), 1, 4, linewidth=1, edgecolor='black', facecolor='lightgrey')
    ax.add_patch(support_arm1)
    ax.add_patch(support_arm2)
    ax.text(3.5, 4, 'Support Arm', rotation=90, verticalalignment='center')

    # Draw the springs
    spring1 = patches.FancyBboxPatch((3, 2), 1, 0.5, boxstyle="round,pad=0.1", linewidth=1, edgecolor='black', facecolor='none')
    spring2 = patches.FancyBboxPatch((6, 2), 1, 0.5, boxstyle="round,pad=0.1", linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(spring1)
    ax.add_patch(spring2)
    ax.text(3.5, 2.3, 'Spring', rotation=90, verticalalignment='center')

    # Draw the compressor
    compressor = patches.Rectangle((4, 6), 2, 3, linewidth=1, edgecolor='black', facecolor='blue')
    ax.add_patch(compressor)
    ax.text(5, 7.5, 'Compressor', horizontalalignment='center', color='white')

    # Draw the acoustic shield
    shield = patches.FancyBboxPatch((3.75, 5.75), 2.5, 3.5, boxstyle="round,pad=0.1", linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(shield)
    ax.text(5, 9.25, 'Acoustic Shield', horizontalalignment='center')

    # Settings
    plt.xlim(0, 10)
    plt.ylim(0, 12)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

draw_fixture()
