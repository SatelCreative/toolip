from shortuuid import ShortUUID


def get_unique_id(length: int) -> str:
    """A utility function to generate a random ShortUUID of a given length.

    Args:
        length: A required int parameter to specify the length of the generated uuid.

    Returns:
        Returns a random ShortUUID.

    """
    return ShortUUID().random(length=length)
