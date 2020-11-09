# Hufflepuff4Life

## Getting started

Run `./train_model.sh` to train the model.

Run and tweak `./text_generation.sh` to get generated text!

## AWS quick start

You can train the model in your own computer but if you don't own a desktop with a dedicated graphics card and loads of memory it will take a long time. That's why we opted to train the model using a AWS instance with special machine-learning hardware.

Choose an instance type like `g4dn.4xlarge` (priced at ~$1 per hour). With those specs you can expect training a model with ~100mb of data in about 7 hours. Disk size can fill up quickly, so choose at least 64gb. When the instance is running, `ssh` inside and run the following commands to train the model:

1. Clone this repo and navigate to the folder:

```bash
$ git clone git@github.com:ceostroff/Hufflepuff4Life.git
```

2. Enter into the virtualenv:

```bash
$ source env/bin/activate
```

3. Install pip:

```bash
$ sudo apt-get update && sudo apt-get install python3-pip
```

And the requirements:

```bash
$ pip3 install -r requirements.txt
```

4. Install [CUDA](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86_64). Follow the instructions, and make sure to add CUDA to the PATH. Reboot the instance.

5. Navigate to your home folder and clone https://github.com/huggingface/transformers:

```bash
$ git clone git@github.com:huggingface/transformers.git
```

And install it:

```bash
pip3 install .
```

6. Now you can train the model. Navigate to this folder again and run `train_model.sh` with:

```bash
./train_model.sh
```

It is important to set `--per_device_train_batch_size=1` and same per `--per_device_eval_batch_size=1`. If you increase the value there's a very high chance that the training will run out of memory.

If you don't have the right permissions you can try make the script executable with `chmod +x train_model.sh`.

7. Now, open a terminal in your own computer and copy the files from the server like this (remove your local files first):

```bash
rsync ubuntu@YOUR_AWS_IP:~/Hufflepuff4Life/model/* .`
```

8. Voilà! Now you can turn off the AWS instance and run the text generation step from your own computer with:

```bash
$ ./text_generation.sh
```

You can ammend various parameters, like text length, temperature and a repetition penalty. See the original file with all the options [here](https://github.com/huggingface/transformers/blob/master/examples/text-generation/run_generation.py).

## Python cheatsheet

To activate the virtual environment:

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