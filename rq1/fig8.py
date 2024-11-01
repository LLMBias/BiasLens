import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Directory and file paths
score_dir = "./score"
output_file = os.path.join(score_dir, "score_distribution_pie.csv")

# Initialize counters for each question type and score (1 to 6) across all attributes
score_distribution = {
    "Yes/No": [0] * 6,  # List of counts for scores 1 to 6
    "Choice": [0] * 6,
    "Wh": [0] * 6
}

# Process each score file in the directory
for attribute_file in os.listdir(score_dir):
    if attribute_file.endswith("_questions_score.csv"):
        # Read the attribute score file
        attribute_path = os.path.join(score_dir, attribute_file)
        with open(attribute_path, 'r', encoding='utf-8', errors='ignore') as f:
            attribute_df = pd.read_csv(f)
        
        # Count the scores for each question type
        for question_type in ["Yes/No", "Choice", "Wh"]:
            type_df = attribute_df[attribute_df["Question Type"] == question_type]
            for score in range(1, 7):  # Consider scores 1 to 6
                score_count = (type_df["Score"] == score).sum()
                score_distribution[question_type][score - 1] += score_count  # Use score - 1 for correct index

# Calculate overall percentages for each score level across all question types
# Sum the counts for each score level across Yes/No, Choice, and Wh
overall_counts = [score_distribution["Yes/No"][i] + score_distribution["Choice"][i] + score_distribution["Wh"][i] for i in range(6)]
total_overall_count = sum(overall_counts)
overall_percentage = [round((count / total_overall_count) * 100, 2) for count in overall_counts]

# Convert individual question type counts to percentages
for question_type in score_distribution:
    total_count = sum(score_distribution[question_type])
    if total_count > 0:  # Avoid division by zero
        score_distribution[question_type] = [
            round((count / total_count) * 100, 2) for count in score_distribution[question_type]
        ]

# Set the descriptive labels for each score level
score_labels = [
    'One LLM',
    'Two LLMs',
    'Three LLMs',
    'Four LLMs',
    'Five LLMs',
    'Six LLMs'
]

# Convert the distribution data to a DataFrame with descriptive score labels
distribution_df = pd.DataFrame(score_distribution, index=score_labels)
distribution_df["Overall"] = overall_percentage  # Add the overall percentage column

# Save the distribution to a CSV file
distribution_df.to_csv(output_file, index_label="Score Level")

print("Score distribution calculation complete. Output saved to 'score_distribution_pie.csv'.")

# Load data from the CSV for plotting
distribution_df = pd.read_csv(output_file, index_col="Score Level")

# Extract percentages for each question type
yes_percentage = distribution_df["Yes/No"].tolist()
choice_percentage = distribution_df["Choice"].tolist()
wh_percentage = distribution_df["Wh"].tolist()
overall_percentage = distribution_df["Overall"].tolist()

# Plotting setup
scores = score_labels
colors = ['#f2f2f2', '#e6e6e6', '#cfcfcf', '#a6a6a6', '#7f7f7f', '#4b4b4b']
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 16
plt.rcParams['font.weight'] = 'bold'

# Create pie charts
fig, axs = plt.subplots(1, 4, figsize=(24, 6))

# Yes/No questions pie chart
wedges, texts, autotexts = axs[0].pie(yes_percentage, labels=scores, autopct='%1.1f%%', 
                                      startangle=90, colors=colors, radius=1)
autotexts[-1].set_position((autotexts[-1].get_position()[0], autotexts[-1].get_position()[1] + 0.1))
axs[0].set_title('Yes/No questions', fontsize=18, fontweight='bold', pad=0)

# Choice questions pie chart
axs[1].pie(choice_percentage, labels=scores, autopct='%1.1f%%', startangle=90, colors=colors, radius=1)
axs[1].set_title('Choice questions', fontsize=18, fontweight='bold', pad=0)

# Wh questions pie chart
axs[2].pie(wh_percentage, labels=scores, autopct='%1.1f%%', startangle=90, colors=colors, radius=1)
axs[2].set_title('Wh questions', fontsize=18, fontweight='bold', pad=0)

# Overall pie chart
axs[3].pie(overall_percentage, labels=scores, autopct='%1.1f%%', startangle=90, colors=colors, radius=1)
axs[3].set_title('Overall', fontsize=18, fontweight='bold', pad=0)

# Final adjustments and save
plt.tight_layout()
plt.savefig('./figure/figure_8.png')
plt.show()
