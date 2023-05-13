"""Utilities for writing and reading length-prefix framed messages. Using
length-prefixed framing makes it easier for the reader to determine the
boundaries of each message before passing it to msgspec to be decoded.
"""
# Copyright (c) 2021, Jim Crist-Harif
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import asyncio


async def prefixed_send(stream: asyncio.StreamWriter, buffer: bytes) -> None:
    """Write a length-prefixed buffer to the stream"""
    # Encode the message length as a 4 byte big-endian integer.
    prefix = len(buffer).to_bytes(4, "big")

    # Write the prefix and buffer to the stream.
    stream.write(prefix)
    await stream.drain()

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
