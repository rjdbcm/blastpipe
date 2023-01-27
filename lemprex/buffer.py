# Some utilities for writing and reading length-prefix framed messages. Using
# length-prefixed framing makes it easier for the reader to determine the
# boundaries of each message before passing it to msgspec to be decoded.
import asyncio


async def prefixed_send(stream: asyncio.StreamWriter, buffer: bytes) -> None:
    """Write a length-prefixed buffer to the stream"""
    # Encode the message length as a 4 byte big-endian integer.
    prefix = len(buffer).to_bytes(4, "big")

    # Write the prefix and buffer to the stream.
    stream.write(prefix)
    stream.write(buffer)
    await stream.drain()

async def prefixed_recv(stream: asyncio.StreamReader) -> bytes:
    """Read a length-prefixed buffer from the stream"""
    # Read the next 4 byte prefix
    prefix = await stream.readexactly(4)

    # Convert the prefix back into an integer for the next message length
    n = int.from_bytes(prefix, "big")

    # Read in the full message buffer
    return await stream.readexactly(n)
