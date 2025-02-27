from time import perf_counter


def measure_time(ocr_engine: str):
    """Displays the time spent on processing a file with an OCR engine.

    Args:
        ocr_engine (str): The name of the OCR engine used.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            execution_time = end_time - start_time
            print(f"{ocr_engine} finished processing in {execution_time:.6f} seconds")

            return result

        return wrapper

    return decorator
