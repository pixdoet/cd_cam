import websockets
import asyncio


class Sender:
    def __init__(self):
        self.serverUrl = "http://127.0.0.1:8000"
        self.ip = "127.0.0.1"  # server ip
        self.port = "8088"  # server port
        self.cameraId = 1

    async def bully_detected(self):
        """
        bully_detected - Connect to the central server
        @param ip - IP Address of server
        @param port - Port of server
        """
        async with websockets.connect(
            f"ws://localhost:4896"  # /cameraconnect/?ip={self.ip}&port={self.port}&camId={self.cameraId}"
        ) as ws:
            await ws.send("bully_detected")

    def run_ws(self):
        asyncio.get_event_loop().run_until_complete(self.bully_detected())
