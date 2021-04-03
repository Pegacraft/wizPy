import asyncio

import discover
from wizPy.light import Light


async def main():
    print(await discover.discover())
    light: Light = Light(ip="192.168.0.9")
    light.set_brightness(255)
    light.set_warm_white(100)
    light.on()
    await light.apply()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
