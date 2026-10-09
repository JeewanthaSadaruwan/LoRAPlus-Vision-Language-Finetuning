# LoRAPlus-VLM

Project scaffold for comparing LoRA and LoRA+ when fine-tuning SmolVLM on a
vision-language task.

## Status

The directory structure, starter configuration, and results notebook are in
place. Dataset preprocessing, model loading, training, and evaluation still
need implementation. No experiments have been run or findings recorded.

## Structure

```text
configs/config.yaml         Model, adapter, dataset, and training settings
src/data.py                 Dataset loading and preprocessing scaffold
src/model.py                Model and adapter setup scaffold
src/train.py                LoRA and LoRA+ training scaffold
src/evaluate.py             Evaluation scaffold
notebooks/experiments.ipynb  Metrics exploration
results/metrics.csv         Evaluation results (header only)
results/plots/              Convergence plots
checkpoints/                Adapter checkpoints (ignored by Git)
requirements.txt            Initial Python dependencies
EN4554_Assignment.pdf        Assignment document
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Dependency versions and hardware requirements have not yet been validated.
Set the dataset name and column mappings in `configs/config.yaml` before
implementing the training pipeline. The configuration values are starting
points for experiments.

## Experiments

Implement the modules in `src/`, then run comparable LoRA and LoRA+ experiments
using the same dataset splits, seed, and training budget. For LoRA+, use the
configured learning-rate ratio for the adapter matrix parameter groups.

Record each experiment in `results/metrics.csv`, with accuracy expressed as a
fraction from 0 to 1 and training duration in seconds. Save convergence plots
in `results/plots/` and adapter weights in `checkpoints/`.

To explore recorded metrics:

```bash
jupyter lab notebooks/experiments.ipynb
```

## Findings

Pending completed experiments.
