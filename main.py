import hydra
from pathlib import Path
from omegaconf import OmegaConf, DictConfig


@hydra.main(config_path='conf')
def main(cfg:DictConfig):
    # use code to add config files
    print(OmegaConf.to_yaml(cfg))
    # the output will be seen in .hydra folder

if __name__ == '__main__':
    # use code to add config files
    # please paste the following code into cmd
    str = 'C:\Conda\python.exe main.py +db.dirver=mysql +db.user=omry +db.password=secret'
    main()
