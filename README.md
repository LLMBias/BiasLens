
# Fairness testing of Large Language Models during Role-Playing

Welcome to the online appendix for the paper titled "Benchmarking Bias in Large Language Models during Role-Playing." Here, we provide supplementary materials, including scripts, generated roles, generated questions, LLM-generated answers, and our analysis results. This repository is under the terms of the MIT License.

## Environment Setup

Install dependencies:

```python
pip install -r requirements.txt
```

## Questions

This section contains two parts, both located in the `./questions` folder: **Question Generator** and **Generated Questions**.

The code for generating questions is available in the `./questions` directory. To run the code, use:

```python
python ./question_generator.py
```

> **Note:** Ensure you have entered your OpenAI API key before running the script.

For convenience, we have publicly released all generated questions in the `./questions/role` folder as 11 CSV files. Each attribute includes 50 roles, with each role containing 20 Yes/No questions, 20 Choice questions, and 20 Why questions. This setup means each CSV file holds \(50 \times 3 \times 20 = 3,000\) questions, totaling \(11 \times 3,000 = 33,000\) questions across all attributes.

After reviewing, 136 questions were removed for containing placeholder terms like “Group A” and “Group B” (e.g., "Do you believe Group A are naturally better leaders than Group B?"). The final benchmark now includes 32,864 questions, broken down as follows:

- **10,975 Yes/No questions**
- **10,917 Choice questions**
- **10,972 Why questions**

All questions are organized by attribute in individual CSV files in the `./questions/role` folder. Additionally, questions used in RQ4, which do not specify roles, are available in the `./questions/without_role` folder.

## Query Scripts

This section provides the query scripts for each Large Language Model (LLM), divided into two types: **Role-based Queries** and **Non-role-based Queries**. Role-based queries include role information, while non-role-based queries do not specify roles. Each LLM has a dedicated Python script for each query type. 

For role-based queries, you’ll find 8 Python scripts in the `./query/role` folder. To query a specific model, simply run the corresponding script, e.g.,

```python
python ./query/role/gpt4omini.py
```

For non-role-based queries, use the scripts in the `./query/without_role` folder. For example:

```python
python ./query/without_role/gpt4omini.py
```

> **Note:** Ensure you have obtained an API key from each platform and enter it in the relevant script before querying. Here are the links to obtain API keys for each model:

- **GPT4o-mini**: [https://platform.openai.com/docs/models](#)
- **DeepSeek-v2.5**: [https://api-docs.deepseek.com/](#)
- **Qwen1.5-110B, Llama-3-8B, Llama-3-70B, Mistral-7B-v0.3**: [https://aimlapi.com/app/](#)

> **Cost Notice:** Querying these models may incur costs depending on each platform's usage and pricing policies. Be mindful, as querying large datasets can result in significant charges.


## LLM-generated Answers

This section contains collected answers for both role-based and non-role-based questions. All files are located in the `./answers` folder, with role-based answers in `./answers/role` and non-role-based answers in `./answers/without_role`. All answers are generated directly in response to each question.

For each of the 11 attributes, we generate 50 roles for testing. Each question is individually input into six different LLMs, and to reduce randomness, each question is asked to each LLM three separate times. Each instance is treated as an independent conversation, with no context from previous interactions. This setup allows for three distinct rounds of questioning per LLM.

Additionally, we provide the judging code for each "Why" question in the file located at `./query/why_judge.py`.


## Results Analysis

In this section, we provide all the code and data required to replicate the tables and figures from our study. Specifically, we have scripts for generating:

- **Table 3**: Displays the number of biased responses detected by our benchmark across 11 demographic attributes and 3 question types for 6 LLMs during role-playing. To generate this table, execute:

  ```bash
  python ./table3/table3.py
  ```

  The results will be saved in `./table3/table3.csv`, with more detailed results for each model stored in their respective folders.

- **Figure 7**: Shows the average biased responses per demographic attribute across the six LLMs. To generate this figure, execute:

  ```bash
  python ./figure/fig7.py
  ```

  The output image will be saved as `./figure/figure_7.png`.
- **Figure 8**: Illustrates the proportion of questions that elicit biased responses across one to six LLMs. First, assess each question for biased responses on all six LLMs, with the scores stored in the `score` folder. To calculate these scores, run:

  ```bash
  python ./figure/fig8_data.py
  ```

  Note that this process may take some time. Alternatively, you can skip this step and directly execute the following command, as we have provided the pre-calculated scores for your convenience:

  ```bash
  python ./figure/fig8.py
  ```

  The output image will be saved as `./figure/figure_8.png`.


- **Figure 10**: Shows the bias types in bias-triggering questions. To generate this figure, execute:

  ```bash
  python ./figure/fig10/fig10.py
  ```

  The output image will be saved as `./figure/fig10/figure_10.png`.
  

- **Table 4**: To generate this table, execute:

  ```bash
  python ./table4/table4.py
  ```

  The results will be saved in `./table4/table4.csv`, with more detailed results for each model stored in their respective folders.

- **Comparison of Results**: To compare the results with those from previous analyses, execute:

  ```bash
  python ./table4/comparison.py
  ```

  The comparison results will be saved in `./table4/comparison_result.csv`.

- **Table 5**: To generate this table, run:

  ```bash
  python ./table5/table5.py
  ```

  The results will be saved in `./table5/table5.csv`.






