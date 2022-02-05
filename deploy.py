import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-b","--backend", help="backend update", action="store_true")
group.add_argument("-t","--tensorflow", help="tensorflow update", action="store_true")
group.add_argument("-c","--compose", help="backend update", action="store_true")
group.add_argument("-bc","--backendcompose", help="backend update", action="store_true")
group.add_argument("-tc","--tensorflowcompose", help="backend update", action="store_true")

args = parser.parse_args()


backend=[
    'sudo docker build -t backend:latest ./backend',
]
tfserve=[
    'sudo docker build -t tensorflow-serving:latest ./tf-serve'
]
compose=[
    'sudo docker-compose up'
]
import os
if args.backend or args.backendcompose:
    for cmd in backend:
        os.system(cmd)
    print("Backend Image created")

if args.tensorflow or args.tensorflowcompose:
    for cmd in tfserve:
        os.system(cmd)
    print("Tensorflow/serving Image created")


if args.compose or args.backendcompose or args.tensorflowcompose:
    for cmd in compose:
        os.system(cmd)