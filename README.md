# -ColossalAI_MlpMixer
This project is the reproduction of MlpMixer model with ColossalAI tool.


## Envirionment setup
```
git clone https://github.com/hpcaitech/ColossalAI.git
cd ColossalAI
# install dependency
pip install -r requirements/requirements.txt

# install colossalai
pip install .
```

## Usage

To start training, use the following command to run each worker:
```
$ DATA=/path/to/dataset python train.py --world_size=WORLD_SIZE \
                                        --rank=RANK \
                                        --local_rank=LOCAL_RANK \
                                        --host=MASTER_IP_ADDRESS \
                                        --port=MASTER_PORT \
                                        --config=CONFIG_FILE
```
It is also recommended to start training with torchrun as:

```
$ DATA=/path/to/dataset python train.py --world_size=WORLD_SIZE \
                                        --rank=RANK \
                                        --local_rank=LOCAL_RANK \
                                        --host=MASTER_IP_ADDRESS \
                                        --port=MASTER_PORT \
                                        --config=CONFIG_FILE
```




## Cite us
```
@article{bian2021colossal,
  title={Colossal-AI: A Unified Deep Learning System For Large-Scale Parallel Training},
  author={Bian, Zhengda and Liu, Hongxin and Wang, Boxiang and Huang, Haichen and Li, Yongbin and Wang, Chuanrui and Cui, Fan and You, Yang},
  journal={arXiv preprint arXiv:2110.14883},
  year={2021}
}
```
