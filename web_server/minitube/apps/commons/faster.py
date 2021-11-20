from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS_LIMIT = 50


def do_concurrently(max_workers, func_args_list):
    """
    Args:
        max_workers: maximum threads to spawn
        func_args_list: list of tuple of (func, [arg1, arg2, arg3])

    Returns:
        the response of each function call as a list

    """
    out = []
    futures = []
    max_workers = min(max_workers, MAX_WORKERS_LIMIT)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        for func, args in func_args_list:
            futures.append(executor.submit(func, *args))

        for future in as_completed(futures):
            if future.result() is not None:
                out.append(future.result())

    return out
