<p align="left">
  <img src="docs/images/logo.svg" />
</p>  

# Moovita installation instruction
1. In order to use this repo, you need to use hailo sdk version 3.11 available [here](https://drive.google.com/file/d/1IYQ5MTBTi1zURNNUlWZg6EMXFuZsHT4D/view?usp=sharing). DO NOT USE SDK version 3.13 which is used to compile the networks.
2. Extract the downloaded sdk. 
3. `sudo apt install build-essential bison flex libelf-dev dkms cmake`
4. `cd hailo_sdk`
5. Check system requirements with `./check_system_requirements.sh`. The result is available in system_reqs_results.log.
6. `./install.sh`
7. `source hailo_virtualenv/bin/activate` to activate hailo_virtualenv (Do this everytime you need to use the hailo_model_zoo)

# Splitting yolo output
1. `cd hailo_model_zoo` (root directory)
2. `pip install -e .` to install dependecies
3. `mkdir data`
4. Copy your yolo onnx file to data folder
5. Under `hailo_model_zoo/cfg/networks/`, there is tiny_yolov4_moovita.yaml file with configures the splitting process. You should create a new configuration file with tiny_yolov4_moovita.yaml as reference. The new configuration file must be inside `hailo_model_zoo/cfg/networks/`. Inside this yaml file, there are comments giving instructions on how to change the parameters. You will also be able to specify the path to your onnx file (the path is relative from the data folder).
6. `python hailo_model_zoo/main.py parse <yaml file name without extension>` (e.g `python hailo_model_zoo/main.py parse tiny_yolov4_moovita`)
7. A .har file will be generated. The name of the har file is specified in the .yaml file.
8. Use this har file for quantization (skip the parsing step).

# Hailo Model Zoo #

The Hailo Model Zoo provides pre-trained models for high-performance deep learning applications. Using the Hailo Model Zoo you can measure the full precision accuracy of each model, the quantized accuracy using the Hailo Emulator and measure the accuracy on the Hailo-8 device. Finally, you will be able to generate the Hailo Executable Format (HEF) binary file to speed-up development and generate high quality applications accelerated with Hailo-8. The models are optimized for high accuracy on public datasets and can be used to benchmark the Hailo quantization scheme.

<p align="center">
  <img src="docs/images/tasks.jpg" />
</p>

<br>

## Change Log

<details>
<summary> V1.2 </summary>

- New features:
  - YUV to RGB on core can be added through YAML configuration.
  - Resize on core can be added through YAML configuration.
- Support D2S Dataset
- New task: instance segmentation
  - yolact_mobilenet_v1 (coco)
  - yolact_regnetx_800mf_20classes (coco)
  - yolact_regnetx_600mf_31classes (d2s)
- New models:
  - nanodet_repvgg
  - centernet_resnet_v1_50_postprocess
  - yolov3 - [darkent based](https://github.com/AlexeyAB/darknet)
  - yolox_s_wide_leaky
  - deeplab_v3_mobilenet_v2_dilation
  - centerpose_repvgg_a0
  - yolov5s, yolov5m - original models from [link](https://github.com/ultralytics/yolov5/tree/v2.0)
  - yolov5m_yuv - contains resize and color conversion on HW
- Improvements:
  - tiny_yolov4
  - yolov4
- IBC and Equalization API change
- Bug fixes
</details>

<details>
<summary> V1.1 </summary>

- Support VisDrone Dataset
- New task: pose estimation
  - centerpose_regnetx_200mf_fpn
  - centerpose_regnetx_800mf
  - centerpose_regnetx_1.6gf_fpn
- New task: face detection
  - lightfaceslim
  - retinaface_mobilenet_v1
- New models:
  - hardnet39ds
  - hardnet68
  - yolox_tiny_leaky
  - yolox_s_leaky
  - deeplab_v3_mobilenet_v2
- Use your own network manual for YOLOv3, YOLOv4_leaky and YOLOv5.
</details>

<details>
<summary> V1.0 </summary>

- Initial release
- Support for object detection, semantic segmentation and classification networks
</details>

<br>

## Models

Full list of pre-trained models can be found [**here**](docs/MODELS.md).

<br>

## Benchmarks

List of Hailo's benchmarks can be found in [**hailo.ai**](https://hailo.ai/developer-zone/benchmarks/).
In order to reproduce the measurements please refer to the following [**page**](docs/BENCHMARKS.md).

<br>

## Usage

### Quick Start Guide
* Install the Hailo Dataflow Compiler and enter the virtualenv. In case you are not Hailo customer please contact [**hailo.ai**](https://hailo.ai/contact-us/)
* Clone the Hailo Model Zoo
```
git clone https://github.com/hailo-ai/hailo_model_zoo.git
```
* Run the setup script
```
cd hailo_model_zoo; pip install -e .
```
* Run the Hailo Model Zoo. For example, to parse the ResNet V1 50  model:
```
python hailo_model_zoo/main.py parse resnet_v1_50
```

### Getting Started

For further functionality please see the [**GETTING_STARTED**](docs/GETTING_STARTED.md) page (full install instructions and usage examples). The Hailo Model Zoo is using the Hailo Dataflow Compiler for parsing, model optimization, emulation and compilation of the deep learning models. Full functionality includes:
* Parse: model translation of the input model into Hailo's internal representation.
* Profiler: generate profiler report of the model. The report contains information about your model and expected performance on the Hailo hardware.
* Quantize: optimize the deep learning model for inference and generate a numeric translation of the input model into a compressed integer representation. For further information please see [**OPTIMIZATION**](docs/OPTIMIZATION.md).
* Compile: run the Hailo compiler to generate the Hailo Executable Format file (HEF) which can be executed on the Hailo hardware.
* Evaluate: infer the model using the Hailo Emulator or the Hailo hardware and produce the model accuracy.

For further information about the Hailo Dataflow Compiler please contact [**hailo.ai**](https://hailo.ai/contact-us/).

<p align="center">
  <img src="docs/images/diagram.jpg" />
</p>

### Use Your Own Network

To add a new network to the hailo model zoo please check the following [**guide**](docs/TRAINING_GUIDE.md).

<br>

## License

The Hailo Model Zoo is released under the MIT license. Please see the [**LICENSE**](./LICENSE) file for more information.

<br>

## Contact

Please visit [**hailo.ai**](https://hailo.ai/) for support / requests / issues.