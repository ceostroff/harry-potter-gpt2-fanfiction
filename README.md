# Harry Potter GPT-2 fanfiction generator

```
,-_/,.                   .-,--.     .  .
' |_|/ ,-. ,-. ,-. . .    '|__/ ,-. |- |- ,-. ,-.
 /| |  ,-| |   |   | |    ,|    | | |  |  |-' |      **       *
 `' `' `-^ '   '   `-|    `'    `-' `' `' `-' '       **     **                 zz
                    /|                             **   **  **    ****         zz
                   `-'                               ***   *  *****           zzzzzz
,---. .-,--. ,--,--'                                                             zz
|  -'  '|__/ `- |    ,-,   ," ,-. ,-. ," . ,-.           xx  ****               zz
|  ,-' ,|     , | --  /    |- ,-| | | |- | |            xx      ***            zz
`---|  `'     `-'    '-`   |  `-^ ' ' |  ' `-'         xx
 ,-.|                      '          '               xx                oooooo          oooooo
 `-+'                                                xx                oo    oo        oo    oo
                        .                           xx                 o      oo ***** o      o
,-. ,-. ,-. ,-. ,-. ,-. |- ,-. ,-.                 xx                  o       o**   **o      o
| | |-' | | |-' |   ,-| |  | | |                  xx                   oo     oo       oo     o
`-| `-' ' ' `-' '   `-^ `' `-' '                 xx                     oooooo          oooooo
 ,|
 `'
```

Generate your own Harry Potter fanfiction with a pre-trained GPT-2 generative text model using huggingface's [transformers](https://github.com/huggingface/transformers).

This project has two parts: a scraper and a text generation model. The scraper fetches stories from [fanfiction.net](https://www.fanfiction.net/) and creates text files ready for training.

The text generation bit lets you generate new fanfiction. We have [pre-trained a model](https://huggingface.co/ceostroff/harry-potter-gpt2-fanfiction) using the ~100 most popular HP fanfiction stories, but you can scrape a different set of stories and train your own model.

## Requirements

A computer with Git, Python 3 and pip installed.

## Getting started

First, clone the repo:

```
$ git clone git@github.com:ceostroff/harry-potter-gpt2-fanfiction.git
```

Now, navigate to the folder and install the dependencies (we recommend setting up a `virtualenv`):

```bash
$ pip3 install -r requirements.txt
```

You should have everything you need to run the scraper and the model.

## Generating fanfiction

To run the text generation script first give it permission to run:

```bash
$ chmod +x text_generation.sh
```

Now you can generate text using the default settings and the pre-trained model:

```bash
$ ./text_generation.sh
```

The script will ask you for a prompt: this is the initial text the model will use to generate a story. If you edit the file you can adjust the temperature ('randomness' of the generated text, default at `0.7`), the length and the number of stories (by default 20 blobs of 100 characters each). See the original file with all the options [here](https://github.com/huggingface/transformers/blob/master/examples/text-generation/run_generation.py).

## Train your own model with AWS

You can train the model in your own computer but if you don't own a desktop with a dedicated graphics card and loads of memory it will take a long time. That's why we opted to train the model using a AWS instance with special machine-learning hardware.

Choose an instance type like `g4dn.4xlarge` (priced at ~$1 per hour). With those specs you can expect training a model with ~100mb of data in about 7 hours. Disk size can fill up quickly, so choose at least 64gb. When the instance is running, `ssh` inside and run the following commands to train the model:

1. Clone this repo and navigate to the folder:

```bash
$ git clone git@github.com:ceostroff/harry-potter-gpt2-fanfiction.git
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

5. Now you can train the model. Navigate to this folder again and run `train_model.sh` with:

```bash
./train_model.sh
```

It is important to set `--per_device_train_batch_size=1` and same per `--per_device_eval_batch_size=1`. If you increase the value there's a very high chance that the training will run out of memory.

If you don't have the right permissions remember to make the script executable with `chmod +x train_model.sh`.

6. Now, open a terminal in your own computer and copy the files from the server like this (remove the pre-trained model first):

```bash
rsync ubuntu@YOUR_AWS_IP:~/harry-potter-gpt2-fanfiction/model/* .`
```

7. Voilà! Now you can turn off the AWS instance and run the text generation step from your own computer with:

```bash
$ ./text_generation.sh
```

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