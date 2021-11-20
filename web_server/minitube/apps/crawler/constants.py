class CrawlerStatus:
    RUNNING = 'running'
    STOPPED = 'stopped'


class CrawledItemStatus:
    INITIAL_SAVED = 'initial_saved'
    QUEUED_FOR_INDEX = 'queued_for_index'
    INDEXED = 'indexed'
    FAILED_TO_INDEX = 'failed_to_index'
