from pathlib import Path
import argparse
import yaml
from yaml.loader import SafeLoader 

def get_args_parser():
    parser = argparse.ArgumentParser("JEDE")
    parser.add_argument("--path_to_config", "-c", default="", type=str)
    parser.add_argument("--seed", default=5, type=int)
    # train
    parser.add_argument("--run_name", default="", type=str)
    parser.add_argument("--epochs", default=5, type=int)
    parser.add_argument("--bs", default=64, type=int, help="batch size")
    parser.add_argument(
        "--test_size",
        default=0.2,
        type=float,
        help="Between 0 and 1, the fraction of data of data for testing",
    )

    # inference
    parser.add_argument("--inference",'-i', default=False, action="store_true")
    parser.add_argument("--path_to_checkpoint", default="", type=str)
    parser.add_argument("--checkpoint_num", '-cn',
                        default=None,
                        type=int,
                        help="give the checkpoint number")   

    # device
    parser.add_argument("--device",
                        default="cuda",
                        type=str,
                        help="'cuda' or 'cpu'")
    return parser.parse_args()

def read_yamal(file):
    p = Path(file)
    print(p.absolute(), p.exists())
    with open(p.absolute()) as f:
        data = yaml.load(f, Loader=SafeLoader)
        print(data)
    return data


def process_args_and_config_file():
    """Combine the command line with the input config file. Config file overrides command line. """
    args = get_args_parser()
    # print(args)
    config_file_data = read_yamal(args.path_to_config)
    for k in config_file_data.keys():
        print(k)
        if hasattr(args,k):
            setattr(args,k,config_file_data[k])
        else:
            print("--"*20)
            print(f"UNKNOWN CONFIG FILE OPTION ----     {k}")
            print("--"*20)

    # print(args)
    # print(vars(args))
    return args
