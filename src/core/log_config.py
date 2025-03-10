import logging

f_log = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


def configure_logging(
    level=logging.INFO,
    format_log=f_log
):
    logging.basicConfig(
        format=format_log,
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )