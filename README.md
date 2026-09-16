# SMUGRI-COPA

[🤗 tartuNLP/smugri-copa](https://huggingface.co/datasets/tartuNLP/smugri-copa)

LM Evaluation Harness configurations for evaluating SMUGRI-COPA in Võro and Livonian.

## Usage

Tested with `transformers==4.57.1` and `lm_eval==0.4.9.1`.

The `smugricopa_cf` configs use cloze format (CF); `smugricopa_mc` uses multiple-choice format (MCF). 
Each provides zero-shot and 5-shot tasks for Võro and Livonian.

Example evaluation from the repository root:

```bash
TASKS="smugricopa_liv_Latn,smugricopa_vro_Latn,smugricopa_mc_liv_Latn,smugricopa_mc_vro_Latn,smugricopa_liv_Latn_5shot,smugricopa_vro_Latn_5shot,smugricopa_mc_liv_Latn_5shot,smugricopa_mc_vro_Latn_5shot"

lm_eval --model hf \
  --model_args pretrained=${MODEL},dtype=bfloat16,add_bos_token=True \
  --tasks ${TASKS} \
  --include_path ./configs \
  --batch_size ${BATCH_SIZE} \
  --log_samples \
  --show_config \
  --seed 0,1234,1234,1234 \
  --output_path ${OUTPUT_PATH}
```

Set `MODEL`, `BATCH_SIZE`, and `OUTPUT_PATH` before running.

## Citation
Citation information is coming soon.
