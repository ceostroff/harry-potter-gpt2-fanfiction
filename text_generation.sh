python run_generation.py \
    --model_type=gpt2 \
    --model_name_or_path=ceostroff/harry-potter-gpt2-fanfiction \
    --length=60 \
    --temperature=0.7 \
    --repetition_penalty=3 \
    --num_return_sequences=10