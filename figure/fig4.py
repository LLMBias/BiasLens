import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# Set Arial font
plt.rcParams['font.family'] = 'Arial'

# Create bold font style
font_bold = FontProperties(family='Arial', weight='bold')

# Data input
data = {
    'Attribute': ['Ability', 'Age', 'Body', 'Character', 'Culture', 'Gender', 'Occupation', 'Race', 'Religion', 'Social', 'Victim'],
    'GPT4o-mini': [[71, 460, 562], [108, 481, 565], [91, 350, 589], [108, 463, 549], [118, 614, 717], [98, 456, 459], [120, 424, 626], [117, 582, 739], [94, 307, 619], [90, 433, 565], [100, 400, 569]],
    'DeepSeek': [[13, 618, 631], [29, 726, 580], [9, 486, 644], [26, 725, 608], [28, 816, 764], [12, 691, 509], [22, 645, 639], [12, 834, 800], [17, 635, 622], [21, 662, 590], [20, 523, 609]],
    'Qwen': [[15, 70, 473], [37, 166, 464], [9, 486, 644], [36, 133, 408], [31, 277, 656], [20, 85, 381], [41, 138, 465], [21, 221, 653], [53, 98, 513], [26, 106, 413], [35, 78, 502]],
    'Llama3-8b': [[91, 910, 487], [146, 944, 511], [133, 864, 645], [161, 911, 489], [131, 927, 623], [119, 806, 426], [145, 875, 551], [163, 960, 671], [142, 878, 559], [132, 853, 494], [90, 657, 469]],
    'Llama3-70b': [[47, 480, 400], [105, 543, 482], [62, 433, 507], [83, 543, 414], [109, 719, 648], [70, 443, 360], [98, 482, 492], [99, 782, 696], [107, 467, 539], [73, 485, 453], [81, 311, 394]],
    'Mistral': [[29, 269, 421], [72, 327, 340], [30, 151, 422], [86, 325, 401], [75, 384, 592], [71, 268, 318], [67, 282, 421], [103, 353, 594], [109, 306, 428], [75, 296, 407], [79, 240, 441]]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total for each attribute across all models
totals = []
for attr in df['Attribute']:
    total_yes_no = sum([df[model][df['Attribute'] == attr].iloc[0][0] for model in df.columns[1:]])
    total_choice = sum([df[model][df['Attribute'] == attr].iloc[0][1] for model in df.columns[1:]])
    total_wh = sum([df[model][df['Attribute'] == attr].iloc[0][2] for model in df.columns[1:]])
    totals.append((total_yes_no + total_choice + total_wh)/6)

# Sort attributes by total value in descending order
sorted_data = sorted(zip(df['Attribute'], totals), key=lambda x: x[1], reverse=True)
sorted_attributes, sorted_totals = zip(*sorted_data)

# Plot setup
fig, ax = plt.subplots(figsize=(18, 8))

x = np.arange(len(sorted_attributes))
width = 0.6
color = '#333333'  # Single color for bars

# Draw the bars
bars = ax.bar(x, sorted_totals, width, color=color, label='Total BAC')

# Set labels and title
ax.set_xticks(x)
ax.set_xticklabels(sorted_attributes, rotation=45, ha='right', fontsize=14, fontproperties=font_bold)
ax.set_ylabel('Total $BAC$', fontsize=18, fontproperties=font_bold)

# Set y-axis range with some extra space
ax.set_ylim(0, max(sorted_totals) * 1.1)

# Set font size for ticks
ax.tick_params(axis='both', which='major', labelsize=14)

# Add legend
ax.legend(['Total BAC'], loc='upper right', fontsize=18, prop=font_bold)

# Add value labels on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.0f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=14, fontproperties=font_bold)

autolabel(bars)

plt.tight_layout()

# Save the plot
plt.savefig('./figure/figure_7.png', dpi=300, bbox_inches='tight')

plt.show()
