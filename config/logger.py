import logging


logging.basicConfig(
    level=logging.INFO,
    format="[{asctime}] #{levelname:8}{filename}:"
           "{lineno} - {name} - {message}",
    style="{"
)

logger = logging.getLogger(__name__)