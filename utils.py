import os
import logging

# Create a custom logger
logger = logging.getLogger(__name__)


def get_files_with_extension(directory: str, extension: str):
  """
    Helper function to get all files with a certain extension from a directory.
    """
  logger.info(f"Getting all .{extension} files from {directory}")
  return [
    os.path.join(directory, f) for f in os.listdir(directory)
    if f.endswith(f'.{extension}')
  ]
