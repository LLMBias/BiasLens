# Benchmarking Bias in Large Language Models during Role-Playing

Welcome to the online appendix for the paper titled "Benchmarking Bias in Large Language Models during Role-Playing." Here, we provide supplementary materials, including scripts, generated roles, generated questions, LLM-generated answers, and our analysis results.

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

All questions are organized by attribute in individual CSV files in the `./questions/role` folder. Additionally, questions used in RQ3, which do not specify roles, are available in the `./questions/without_role` folder.

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

In total, this process yields:

**32,864 × 6 × 3 = 591,552 responses.**

Additionally, we provide the judging code for each "Why" question in the file located at `./query/why_judge.py`.


## Results Analysis

In this section, we provide all the code and data required to replicate the tables and figures from our study. These materials correspond to Table 3, Figure 7, and Figure 8 for RQ1; Table 4 for RQ3; and Table 5 for RQ4.


### RQ1

Here, we present the replication results for RQ1, corresponding to Table 3, Figure 7, and Figure 8.

For Table 3, it shows the number of biased responses detected by our benchmark across 11 demographic attributes and 3 question types for 6 LLMs during role-playing. To generate Table 3, execute:

```bash
python ./rq1/table3.py
```

The results will be saved in `./results/role/table3.csv`. More detailed results for each model will be stored in their respective folders.

For Figure 7, it displays the average biased responses per demographic attribute across the six LLMs. To generate Figure 7, execute:

```bash
python ./rq1/fig7.py
```

The output image will be saved as `./figure/figure_7.png`.

For Figure 8, which illustrates the proportion of questions that elicit biased responses across one to six LLMs, we first assess each question for biased responses on all six LLMs. The scores for each question are stored in the `score` folder. To calculate these scores, run the following file (note that this process may take some time):

```bash
python ./rq1/fig8_data.py
```

Alternatively, you can **skip** previous step and directly execute the following command, as we have provided the pre-calculated scores for your convenience:

```bash
python ./rq1/fig8.py
```

The output image will be saved as `./figure/figure_8.png`.


### RQ3

This section contains the replication results for RQ3, corresponding to Table 4.

To generate Table 4, execute

```bash
python ./rq3/table4.py
```

The results will be saved in `./results/without_role/table4.csv`. More detailed results for each model will be stored in their respective folders within `./results/without_role`.

To compare these results with those from RQ1, you can execute the following command:

```bash
python ./rq3/comparison.py
```

The comparison results will be saved in `./rq3/comparison_result.csv`.



### RQ4

In this section, we present the replication results for RQ4, corresponding to Table 5.

To generate Table 5, run:

```bash
python ./rq4/table5.py
```

The results will be saved in `./rq4/table5.csv`.






