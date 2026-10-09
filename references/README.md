# Research references

| Reference | Links | Purpose |
| --- | --- | --- |
| LoRA: Low-Rank Adaptation of Large Language Models | [Paper](https://arxiv.org/abs/2106.09685) · [PDF source](https://arxiv.org/pdf/2106.09685) · [Local PDF](LoRA_Paper.pdf) | Foundation for low-rank adapters and the LoRA baseline. |
| LoRA+: Efficient Low Rank Adaptation of Large Models | [Paper](https://arxiv.org/abs/2402.12354) · [PDF source](https://arxiv.org/pdf/2402.12354) · [Local PDF](LoRAPlus_Paper.pdf) | Explains using different learning rates for the two adapter matrices and informs the LoRA+ comparison. |
| Official LoRA+ implementation | [GitHub](https://github.com/nikhilgsh/loraplus) · Local clone: `external/loraplus/` | Reference for the original optimizer configuration and experiments. |

Our main implementation will use Hugging Face PEFT rather than directly
importing the original LoRA+ repository. The external clone is for study only;
no dependencies are installed as part of this reference setup.

The research PDFs and this README belong in version control.
`references/external/` is excluded by the root `.gitignore`. To recreate the
external clone after checking out this project, run from the project root:

```bash
git clone https://github.com/nikhilgsh/loraplus references/external/loraplus
```
