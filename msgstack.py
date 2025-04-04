"""
    msgstack.py - better rewrite of websocket system to broadcast messages
"""

from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

clients = []


class Camera(WebSocket):
    def handleConnected(self):
        print(f"{self.address} connected.")
        clients.append(self)

    def handleMessage(self):
        print(self.data)
        if self.data == "crowd_detected":
            print("Crowd Detected! Send crowd_detected string to all clients")
            for client in clients:
                if client != self:
                    client.sendMessage(self.data)

    def handleClose(self):
        print(f"Connection from {self.address} closed")


server = SimpleWebSocketServer("127.0.0.1", 8088, Camera)
server.serveforever()
