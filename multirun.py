import hydra
from pathlib import Path
from omegaconf import OmegaConf, DictConfig

@hydra.main(config_path='conf',config_name='config')
def main(cfg:DictConfig):
    print(OmegaConf.to_yaml(cfg))


if __name__ == '__main__':
    # by using a structured config files, you can use the config as you want.
    main()