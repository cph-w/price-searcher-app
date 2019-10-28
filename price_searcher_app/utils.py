import logging
import time


logger = logging.getLogger(__name__)


def log_time(fn):
    def timed(*args, **kw):
        logger.warn(f'Performing action: <{fn.__name__}>')
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        logger.warn(f'Action complete: <{fn.__name__}> ran in {te - ts}s')
        return result
    return timed
