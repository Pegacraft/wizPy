import asyncio

import discover
from light import Light


async def main():
    print(await discover.discover())
    # light: Light = Light(ip="192.168.0.233")
    # light.set_brightness(100)
    # light.set_rgb(r=255, b=100)
    # light.on()
    # await light.apply()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
