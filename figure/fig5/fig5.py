import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# 设置字体
plt.rcParams['font.family'] = 'Arial'  # 统一设置字体为Arial
plt.rcParams['axes.unicode_minus'] = False  # 处理负号问题

# 读取所有csv文件路径
folder_path = './attribute'
files = [
    'ability_questions_answers.csv', 'age_questions_answers.csv', 'body_questions_answers.csv',
    'character_questions_answers.csv', 'culture_questions_answers.csv', 'gender_questions_answers.csv',
    'occupation_questions_answers.csv', 'race_questions_answers.csv', 'religion_questions_answers.csv',
    'social_questions_answers.csv', 'victim_questions_answers.csv'
]

# 11个属性对应的文件命名部分
attributes = ['ability', 'age', 'body', 'character', 'culture', 'gender', 'occupation', 'race', 'religion', 'social', 'victim']

# 存储各个csv文件的数据
data = {}
for file in files:
    data[file] = pd.read_csv(os.path.join(folder_path, file))

# 计算Answer的交集部分
def get_intersection(row):
    answer1 = set(str(row['Answer 1']).split(','))
    answer2 = set(str(row['Answer 2']).split(','))
    answer3 = set(str(row['Answer 3']).split(','))

    answer1 = {item.strip() for item in answer1}
    answer2 = {item.strip() for item in answer2}
    answer3 = {item.strip() for item in answer3}

    return answer1 & answer2 & answer3

# 为每个CSV文件添加一个新的列 'Answer'，包含Answer 1, Answer 2, Answer 3的交集
for file in files:
    data[file]['Answer'] = data[file].apply(get_intersection, axis=1)


# 统计Answer的分布
answer_counts_score3 = Counter()
answer_per_file_score3 = {file: Counter() for file in files}

for file in files:
    file_data = data[file][data[file]['Score'] >= 3]  # 过滤 Score ≥ 3 的数据
    for answer in file_data['Answer']:
        for attr in answer:
            if attr in attributes:
                answer_counts_score3[attr] += 1
                answer_per_file_score3[file][attr] += 1

file_names = [file.split('_')[0] for file in files]


answer_matrix_score3 = pd.DataFrame({attr: [answer_per_file_score3[files[i]].get(attr, 0) for i in range(len(files))] for attr in attributes})
answer_matrix_score3.index = file_names  # 将索引设置为文件名

plt.figure(figsize=(12, 10))
ax = sns.heatmap(answer_matrix_score3, annot=True, cmap='Greys', fmt='d', xticklabels=attributes, yticklabels=file_names, annot_kws={"fontsize":16, "fontweight":'bold'})

# 设置标题和轴标签加粗
plt.xlabel('11 bias types triggered by BiasLens', fontsize=18, fontweight='bold')
plt.ylabel('11 demographic attributes associated with role-based generated questions', fontsize=18, fontweight='bold', labelpad=12)


# 设置刻度字体加粗
plt.xticks(rotation=30, fontsize=16, fontweight='bold')
plt.yticks(rotation=30, fontsize=16, fontweight='bold')

# 设置 colorbar (频率图例) 加粗
colorbar = ax.collections[0].colorbar
colorbar.ax.yaxis.set_tick_params(labelsize=16)  # 调整图例数字大小
for label in colorbar.ax.get_yticklabels():
    label.set_fontweight('bold')  # 使图例数字加粗

plt.tight_layout()
plt.savefig('./fig5.png', dpi=300)
plt.show()