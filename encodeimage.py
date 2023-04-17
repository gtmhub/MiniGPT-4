import argparse
from PIL import Image

from minigpt4.common.config import Config
from minigpt4.models import MiniGPT4
from minigpt4.processors import Blip2ImageEvalProcessor


def parse_args():
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument("--cfg-path", required=True, help="path to configuration file.")
    parser.add_argument(
        "--options",
        nargs="+",
        help="override some settings in the used config, the key-value pair "
        "in xxx=yyy format will be merged into config file (deprecate), "
        "change to --cfg-options instead.",
    )
    args = parser.parse_args()
    return args

print('Initializing Chat')
cfg = Config(parse_args())

model_config = cfg.model_cfg
model = MiniGPT4.from_config(model_config)

vis_processor_cfg = cfg.datasets_cfg.cc_sbu_align.vis_processor.train
vis_processor = Blip2ImageEvalProcessor.from_config(vis_processor_cfg)

raw_image = Image.open("profile.jpeg").convert('RGB')
image = vis_processor(raw_image).unsqueeze(0)

image_emb, _ = model.encode_img(image)