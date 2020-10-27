# Hufflepuff4Life

To activate the virtual enviroment:

```bash
$ source env/bin/activate
```

To update the requirements:

```
$ pip freeze > requirements.txt
```

To install the dependencies

```bash
$ pip install -r requirements.txt
```

## How to run on AWS

Choose an instance type like `g4dn.4xlarge`. Disk size counts, it can fill up quickly, so choose at least 64gb.

1. Install CUDA
2. Clone this repo
3. Enter into the virtualenv
4. Install the requirements
5. Clone https://github.com/huggingface/transformers and pip install it
6. Run `train_model.sh`. It is important to set ` --per_device_train_batch_size=1` to 1 and same per `--per_device_eval_batch_size=1`.
7. Now copy the files on the model folder to your local machine (not the checkpoints), like this `scp ubuntu@ip:~/Hufflepuff4Life/model/* Hufflepuff4Life/`