"""BSD-3-Clause-Attribution Sequence manipulation.
Copyright (c) 2023 Ross J. Duff MSc
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software without
    specific prior written permission.
    4. Redistributions of any form whatsoever must retain the following acknowledgment:
    'This product includes software developed by the
    Peculiar Software Company LLC (http://www.github.com/rjdbcm/).'

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import asyncio
from typing import Set

from .tailcall import async_tail_call


async def _chr_union(*args) -> Set[str]:
    """creates a set of all characters in the union of the given chars"""
    chars = set()
    if len(args) == 2 and all(map(isinstance, args, (int,) * len(args))):
        start, stop = args
        chars |= {chr(i) for i in range(start, stop)}
    else:
        for i in args:
            if isinstance(i, int):
                chars |= {chr(i)}
            elif len(i) == 2 and all(map(isinstance, i, (int,) * len(i))):
                return i  # async_tail_call(chr_union, i)
            else:
                raise TypeError(f"Expected Sequence or int, got {type(i)}")
    return chars


def chr_union(*args):
    """Wraps an asynchronous sequence of int ranges or ints into a set of str
    :author: Ross J. Duff MSc
    :return: a set of chr()
        1. range(start=args[0], stop=args[1])
            OR
        2. chr(arg[n] if type(arg[n])==int) | chr_union(arg[:2])
    :raises: ValueError
        if not a sequence of start,stop pairs and ints, an int, or a start, stop pair
    """
    return asyncio.run(async_tail_call()(_chr_union)(*args))
