from shortuuid import ShortUUID


def get_unique_id(length: int) -> str:
    """A utility function to generate a random ShortUUID of a given length.

    Args:
        length: Length of the randomly generated UUID.

    Returns:
        Returns a random ShortUUID.

    """
    return ShortUUID().random(length=length)
