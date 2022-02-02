import argparse
import torch
from data import set_cfg
from export_config import ExportConfig
from torch.autograd import Variable

from yolact import Yolact


def main(args):
    if args.config is not None:
        set_cfg(args.config)
    ExportConfig().onnx = True
    net = Yolact()
    net.load_weights(args.trained_model)
    net.eval()

    dummy_input = Variable(torch.randn(1, 3, 512, 512))
    opsetver = 11
    torch.onnx.export(net,
                      dummy_input,
                      args.export_path,
                      opset_version=opsetver,
                      verbose=False)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description='YOLACT COCO Evaluation')
    parser.add_argument('--config', default=None,
                        help='The config object to use.')
    parser.add_argument('--trained_model',
                        default='weights/ssd300_mAP_77.43_v2.pth', type=str,
                        help='Trained state_dict file path to open. If "interrupt", this will open the interrupt file.')
    parser.add_argument('--export_path',
                        type=str, help='Path to save .onnx file to, including onnx name endinf with ".onnx".')
    args = parser.parse_args(argv)
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
