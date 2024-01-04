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
