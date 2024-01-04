[English (英语)](./README.md)

# circuitpython-easydisplay
- 适用于 `CircuitPython` 的：高通用性，多功能，纯 `CircuitPython` 实现的显示库

### 显示效果
以下为 `1.0` 版本的显示效果
![IMG_20240104_141624](https://github.com/funnygeeker/circuitpython-easydisplay/assets/96659329/7bec666b-bbb6-43e6-91af-3c1cf7103037)

### 项目特点
- 可以通过导入 `bmf` 字体文件，显示非 `ASCII` 字符，比如：中文 和 特殊符号
- 支持 `P4`/`P6` 格式的 `PBM` 图片显示，以及 `24-bit` 的 `BMP` 图片显示
- 初始化时可以设置默认参数，调用函数时更简洁，同时调用指定函数时，本次调用可覆盖默认参数

### 使用方法
- 详见源码注释

### 注意事项
`dat` 格式的图片在非 Framebuffer 驱动模式下，不得超出屏幕显示范围，否则图像可能无法正常显示

### 示例代码
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
ed = EasyDisplay(display=dp, font="/text_lite_16px_2312.v3.bmf", show=True, color=1, clear=True,
                 color_type="MONO", key=0)

ed.bmp("/img/test.bmp", 0, 0)
time.sleep(3)
ed.pbm("/img/test.pbm", 0, 0, color_type="MONO")
time.sleep(3)
ed.text("你好，世界！\nHello World!\nこんにちは、世界！", 0, 0)

# 更多高级使用方式详见源码注释：/lib/easydisplay.py
# For more advanced usage, please refer to the source code comments: /lib/easydisplay.py
```

### 注意事项
- 该项目从 [micropython-easydisplay](https://github.com/funnygeeker/micropython-easydisplay) 移植，目前处于早期版本。
- 受限于 circuitpython 的 adafruit_framebuf，运行效率会比 micropython 上更慢，目前并没有进行完整的功能性验证，可能存在着大量 BUG，使用时请慎重。
