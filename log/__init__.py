import logging

# Create a custom logger
logger = logging.getLogger(__name__)
minimum_type_logger = logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('all_project_logs.log')
console_handler.setLevel(logging.WARNING)
# i want all the logs to be written in a file and the critical ones to the consule as well
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def debug_log(class_name: str, func_name: str, message: str):
    logger.name = class_name
    logger.debug(f"in {func_name} function : {message}")


def info_log(class_name: str, func_name: str, message: str):
    logger.name = class_name
    logger.info(f"in {func_name} function : {message}")


def warning_log(class_name: str, func_name: str, message: str):
    logger.name = class_name
    logger.warning(f"in {func_name} function : {message}")


def error_log(class_name: str, func_name: str, message: str):
    logger.name = class_name
    logger.error(f"in {func_name} function : {message}")
