# Wizpy

## Install

`pip install wizpy`

## How to use

### Example: 

```python
import asyncio
from time import sleep

from wizPy import discover
from wizPy.light import Light


async def main():
    for ip in await discover.discover():
        light: Light = Light(ip)
        light.off()
        await light.apply()
        print(f"light blinking: {ip}")
        sleep(1)
        light.on()
        light.set_brightness(255)
        await light.apply()
        sleep(1)
        light.off()
        await light.apply()
```

To set or get the state of an light, you need to create a `Light` object, with the IP of the light. 

The light class has getter and setter to change the state of the light or get further information about it.

If you wanna apply changes, use `apply()` to send the updated state to the bulb.

To retrieve the IPs of the lights you can use the `discover()` method. If everything worked, this method will return a list containing all the IPs as strings.
