
# Image Sticker Effect

This project adds a smooth white border around transparent areas of an image to create a sticker-like effect.

## Configuration

To adjust the effect, modify the parameters in `config.json`:

- `dilation_kernel_size`: Size of the kernel used for dilation. Must be a list of two integers. Default is [3, 3].
- `dilation_iterations`: Number of times dilation is applied. Default is 2.
- `epsilon_factor`: Multiplier for contour approximation accuracy. Smaller values give a more accurate approximation. Default is 0.006.
- `border_thickness`: Thickness of the white border to be drawn. Default is 10.

## Installation

To set up your environment to run the script, you need to install the required dependencies:

1. Open a command prompt window in the project's root directory.
2. Run the `run-install.bat` file by typing:

```shell
run-install.bat

## Usage

1. Adjust the parameters in `config.json` as desired.
2. Run the script with the image path and the output path provided.

```python
add_white_sticker_effect('path_to_your_image.png', 'path_to_save_output_image.png')
```

The script will read the image, process it according to the parameters, and save the output image with a smooth white border.
