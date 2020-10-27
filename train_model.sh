export TRAIN_FILE=data/trimmeddata.txt
export TEST_FILE=data/testdata.txt

python run_language_modeling.py \
    --output_dir=model/ \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --do_eval \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1 \
    --eval_data_file=$TEST_FILE
