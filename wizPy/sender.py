import asyncio
import json

import asyncio_dgram


async def receive_udp(stream, timeout: int) -> str:
    """Get message with timout value."""
    data, remote_addr = await asyncio.wait_for(stream.recv(), timeout)
    return data


async def send_udp(ip: str, message: str) -> str:
    """Send the UDP message to the bulb."""
    # overall 10 sec. for time out
    timeout = 2
    send_interval = 0.5
    max_send_datagrams = 2
    port = 38899

    try:
        stream = await asyncio.wait_for(asyncio_dgram.connect((ip, port)), timeout)
        receive_task = asyncio.create_task(receive_udp(stream, timeout, ))
        i = 0
        while not receive_task.done() and i < max_send_datagrams:
            asyncio.create_task(stream.send(bytes(message, "utf-8")))
            await asyncio.sleep(send_interval)
            i += 1

        await receive_task
        data = receive_task.result()
    finally:
        try:
            stream.close()
        except UnboundLocalError:
            raise ConnectionError("Bulb is offline or IP address is not correct.")
    if data is not None and len(data) is not None:
        return data.decode()


async def send(ip: str, request: json) -> json:
    try:
        to_send: json = await send_udp(ip, json.dumps(request))
        return to_send
    except:
        print("Could not communicate")
