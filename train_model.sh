export TRAIN_FILE=data/training.txt
export TEST_FILE=data/test.txt

python run_clm.py \
    --output_dir model/ \
    --model_name_or_path gpt2 \
    --do_train \
    --train_file $TRAIN_FILE \
    --do_eval \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1 \
    --validation_file=$TEST_FILE \
    --save_total_limit=5 \
    --overwrite_output_dir

