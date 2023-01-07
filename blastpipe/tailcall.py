from ast import Call
from typing import Annotated, Callable, Collection, Coroutine, Tuple, TypeAlias, Mapping, Optional
import functools
TailCallFlag: TypeAlias = Tuple[()]
TailCallDecor: TypeAlias = Annotated[Optional[TailCallFlag], '@tail_call()']
TAIL_CALL: TailCallFlag = tuple() # PEP 484 Empty Tuple

DecoratedCallable: TypeAlias = Annotated[Callable, TailCallDecor]

def async_tail_call(tuple_return=True) -> DecoratedCallable:
    """https://gist.github.com/orf/41746c53b8eda5b988c5
    CHANGES: tuple_return defaults to True
    Not deprecated as of Python 3.11.1
    """
    def __wrapper(func):

        async def _optimize_partial(*args, **kwargs):
            """
            I replace the reference to the wrapped function with a functools.partial object
            so that it doesn't actually call itself upon returning, allowing us to do it instead.
            Advantages: Theoretically needs no code changes and is more understandable
            Disadvantages: Its startup overhead is higher and its a bit slower. Also can only call
            recursively when returning, so return func(1) + func(2) will not work.
            """
            old_reference = func.func_globals[func.func_name]
            func.func_globals[func.func_name] = functools.partial(functools.partial, func)

            to_execute = functools.partial(func, *args, **kwargs)

            while isinstance(to_execute, functools.partial):
                to_execute = await to_execute()

            func.func_globals[func.func_name] = old_reference
            return to_execute

        async def _optimize_tuple(*args, **kwargs):
            """
            This way requires the function to return a tuple of arguments to be passed to the next
            call.
            Advantages: Very little overhead, faster than plain recursion
            Disadvantages: Needs code changes, not as readable, no support for keyword arguments (yet)
            """
            while args.__class__ is tuple:  # Faster than isinstance()!
            #while isinstance(args, tuple):
                args = await func(*args)

            return args

        if tuple_return:
            functools.update_wrapper(_optimize_tuple, func)
            return _optimize_tuple
        else:
            functools.update_wrapper(_optimize_partial, func)
            return _optimize_partial

    return __wrapper


@async_tail_call()
def test_fib_optimize(i, current=0, next=1):
    return current if i == 0 else test_fib_optimize(i - 1, next, current + next)


@async_tail_call(tuple_return=True)
def test_fib_tuple_optimized(i, current=0, next=1):
    return current if i == 0 else (i - 1, next, current + next)
