# Utils Module

Contains python utility classes and functions.

## Logs

- `setup_logging`: Sets up logging using `loguru`. Includes logging of uvicorn and fastapi if it exists in the project. Logs are stored in `/python/logs` directory.

**Parameters**

- `logfilename`: is a required str parameter for specifying the filename
- `rotation`: is a required str parameter specifying how long a file's rotation should happen
- `retention`: is a required str parameter specifying how long before a file is cleaned up

See [loguru](https://github.com/Delgan/loguru) for more details.

## Misc

- `get_unique_id`: A utility function to generate a random `ShortUUID` of a given length.

**Parameters**

- `length`: is a required int parameter to specify the length of the generated uuid

## Redoc

## Time

- `now`: Returns the current datetime in utc.
- `now_epoch`: Returns the current datetime in utc epoch format.
- `now_epoch_ms`: Returns the current datetime in ms utc epoch format
- `make_time_aware`: Converts given datetime to utc

**Parameters**

- `dtime`: is a required datetime that will be converted to utc
