import logging
import threading

logger = logging.getLogger(__name__)


class BackgroundTasks(threading.Thread):

    def run(self, *args, **kwargs):
        logger.info(
            'Running task in background: %s', (self._target.__name__
                                               if self._target else None)
        )
        super(BackgroundTasks, self).run()
