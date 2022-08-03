import dataclasses

import hydra
from omegaconf import OmegaConf, DictConfig
from dataclasses import dataclass
from hydra.core.config_store import ConfigStore

@dataclass
class Data_Config:
    tol:float = 1e-6
    big:float = 1e-8

defaults = [
    {'classification':'svm'},
    {'regression': 'ls'},
    {'setup':'params'},
    # {'data':'data_config'},
]

@dataclass
class Default_Config:
    defaults: list = dataclasses.field(default_factory=lambda :defaults)


cs = ConfigStore.instance()
cs.store(group='data',name='data_config',node=Data_Config)
cs.store(name='config',node=Data_Config)

@hydra.main(config_path='conf',config_name='config')
def main(cfg:DictConfig):
    print(OmegaConf.to_yaml(cfg))



if __name__ == '__main__':
    main()