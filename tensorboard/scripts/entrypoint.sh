#! /bin/bash

tensorboard --logdir ${LOGDIR:-$HOME/logs} --bind_all --load_fast=false
