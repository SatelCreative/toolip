from shortuuid import ShortUUID  # type: ignore


def get_unique_id(length: int) -> str:
    return ShortUUID().random(length=length)
