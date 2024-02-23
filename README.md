[简体中文 (Chinese)](./README.ZH-CN.md)

# circuitpython-easydisplay
- A universal, versatile, pure CircuitPython implementation of a display library.

### Display Effects
Below are the display effects of version 1.0.
![IMG_20240104_141624](https://github.com/funnygeeker/circuitpython-easydisplay/assets/96659329/7bec666b-bbb6-43e6-91af-3c1cf7103037)

### Project Features
- Supports displaying non-ASCII characters, such as Chinese and special symbols, by importing `bmf` font files.
- Supports displaying images in `P4`/`P6` format for PBM images and `24-bit` BMP images.
- Allows setting default parameters during initialization for cleaner function calls. Current function calls can override the default parameters.

### Usage
- Refer to the source code comments for details.

### Notes
For `dat` format images, ensure that they do not exceed the screen display range in non-Framebuffer driver mode, otherwise the image may not be displayed correctly.

### Example Code
```python
# 这是一个使用示例 This is an example of usage
import time
import busio
import board
from driver import adafruit_ssd1306
from lib.easydisplay import EasyDisplay

# RP2040 & SSD1306
i2c = busio.I2C(board.GP27, board.GP26)
dp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
ed = EasyDisplay(display=dp, font="/text_lite_16px_2312.v3.bmf", show=True, clear=True, key=0)

ed.bmp("/img/test.bmp", 0, 0)
time.sleep(3)
ed.pbm("/img/test.pbm", 0, 0)
time.sleep(3)
ed.text("你好，世界！\nHello World!\nこんにちは、世界！", 0, 0)

# 更多高级使用方式详见源码注释：/lib/easydisplay.py
# For more advanced usage, please refer to the source code comments: /lib/easydisplay.py
```

### Notes
- This project is a port from [micropython-easydisplay](https://github.com/funnygeeker/micropython-easydisplay) and is currently in an early version.
- Due to the limitation of Adafruit's adafruit_framebuf in CircuitPython, the runtime efficiency is slower compared to MicroPython. It has not undergone full functional verification, so there may be many bugs. Please use with caution.
