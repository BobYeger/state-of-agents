# Skill Augmented GRPO for self-Evolution
This repository contains the official implementation of **SAGE (Skill Augmented GRPO for self-Evolution)**, introduced in our paper [Reinforcement Learning for Self-Improving Agent with Skill Library](https://arxiv.org/pdf/2512.17102).

## 📖 Algorithm Preview
The figure below illustrates the Skill Library Agent and **Sequential Rollout with Skill-integrated Reward**, a core component of SAGE on which GRPO is applied.


## ⚙️ Building Modified Dependencies
SAGE depends on two modified open-source repositories: [appworld](https://github.com/StonyBrookNLP/appworld) and [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). The modifications are provided in the `patches/appworld` and `patches/LLaMA-Factory` directories. Please follow the instructions below to build these modified dependencies.
#### 1. appworld Setup
```
# Install git lfs (appworld required)
apt-get update
apt-get install -y --no-install-recommends git-lfs

# Clone repositories
git clone https://github.com/StonyBrookNLP/appworld.git
git -C appworld checkout 57253350edf00922f370a8c7dbe94f1a4d3ee456

# Apply modifications
cp -r patches/appworld/* appworld/
```
#### 2. LLaMA-Factory Setup
```
# Clone repositories
git clone https://github.com/hiyouga/LLaMA-Factory.git
git -C LLaMA-Factory checkout 2c6aded5d4f4ff23aa1887d16972afb3c2543ac3

# Apply modifications
cp -r patches/appworld/* appworld/
```

## 📂 Repository Structure
After building the modified dependencies, the final repository has the following strucrue:

**`sage/`** - Main SAGE algorithm implementation (requires AppWorld installation).

**`appworld/`** - AppWorld environment setup and Skill Library Agent evaluation.
→ Evaluation code located at: `appworld/experiments/code/skill_library_agent/`

**`LLaMA-Factory/`** - Code for Supervised Fine-Tuning (SFT).


## 🚀 Running SAGE
#### 1. SAGE Environment Setup
Install the python environment for SAGE:
```bash
# Create the virtual python environment
cd sage
uv venv appworld_sage --python 3.11
source appworld_sage/bin/activate

# Install dependencies for sage
uv pip install --no-deps -r requirements.txt
uv pip install -e .

# Install flash attention 2
cd ..
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
uv pip install --no-build-isolation .

# Install appworld
cd ../appworld
uv pip install .
# Also install appworld_experiment
cd experiments
uv pip install .
# Fully install appworld
cd ..
appworld install
# Download appworld data
cd ../sage
appworld download data
```

#### 2. Ray Launch for SAGE
Before running the sage script, launch ray on each compute node:
```bash
# Launch ray on the head node
ray start --head

# Launch ray on other nodes
ray start --address='HEAD_NODE_IP'
```

#### 2. Launch SAGE Training
Start reinforcement learning by running the script after specifying the Ray head node IP and the SFT model path in `run_sage_2nodes.sh`. The training requires at least 2xNVIDIA H100 8-GPU nodes.
```bash
sh run_sage_2nodes.sh
```


## 📊 AppWorld Evaluation
#### 1. AppWorld Setup
For AppWorld evaluation, you need to first deploy the model for evaluation with `vllm`. Since the `vllm` within `appworld_sage` environment is the old version, a new environment with updated version of `vllm` is required for optimal performance:
```bash
uv venv appworld_eval --python 3.12
source appworld_eval/bin/activate
uv pip install vllm --torch-backend=auto
cd appworld
uv pip install -e .
cd experiments
uv pip install -e .
cd ..
appworld install
appworld download data
```
#### 2. Deploy vllm Server
Deploy the model for evaluation with `vllm`, which requires 1xNVIDIA A100 8-GPU node. Remember to replace the `vllm` server url in `appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.
```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m vllm.entrypoints.openai.api_server --model MODEL_PATH --served-model-name sage --tensor-parallel-size 8 --dtype auto --port 2638 &
```
#### 3. Launch AppWorld Evaluation
Run the following commands to perform the appworld evaluation and get results:
```bash
# Start evaluation
appworld run sage_test_normal --config-name sage_test_normal > sage_test_normal.log
# Obtain results
appworld evaluate sage_test_normal
```


## 🛠️ Supervised Fine-tuning
To reach the optimal performance on AppWorld, Supervised Fine-tuning (SFT) with expert experience dataset generation is still required. Thus, here we also provide the data generation pipeline and SFT code for reference.
#### 1. Generate Expert Experience Dataset
The expert experience dataset in our paper is generated with Claude 3.5 Sonnet V2. The environment `appworld_eval` is still used for dataset generation. Before running the data generation script, you should first depoly the Claude model with `litellm` and replace the server url in `appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.
```bash
source appworld_eval/bin/activate
cd appworld
litellm --config litellm_config.yaml    # Set your aws api key in litellm_config.yaml
bash expert_dataset_generation_claude.sh
```

#### 2. Launch SFT
SFT is performed under `LLaMA-Factory` repository. The training requires at least 4xNVIDIA H100 8-GPU nodes.
```bash
# Install the environment for LLaMA-Factory
cd LLaMA-Factory
uv venv llama-factory --python 3.11
source llama-factory/bin/activate
uv pip install -e ".[torch,metrics]" --no-build-isolation

# Lauch the SFT (with slurm script)
sbatch run_sft.sh
```


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the CC BY-NC 4.0 License.


## Notification
This code is being released solely for academic and scientific reproducibility purposes, in support of the methods and findings described in the associated publication. Pull requests are not being accepted in order to maintain the code exactly as it was used in the paper, but interested parties are encouraged to open an issue requesting open source community development.


## Citation
Please cite our paper if you find this repository helpful:
```
@misc{wang2025reinforcementlearningselfimprovingagent,
      title={Reinforcement Learning for Self-Improving Agent with Skill Library},
      author={Jiongxiao Wang and Qiaojing Yan and Yawei Wang and Yijun Tian and Soumya Smruti Mishra and Zhichao Xu and Megha Gandhi and Panpan Xu and Lin Lee Cheong},
      year={2025},
      eprint={2512.17102},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2512.17102},
}
```
