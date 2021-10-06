# Utils Module

Contains python utility classes and functions.

## Logs

- `setup_logging`: Sets up logging using `loguru`. Includes logging of uvicorn and fastapi if it exists in the project. Logs are stored in `/python/logs` directory.

**Parameters**

- `logfilename`: is a required str parameter for specifying the filename.
- `rotation`: is a required str parameter specifying how long a file's rotation should happen
- `retention`: is a required str parameter specifying how long before a file is cleaned up

See [loguru](https://github.com/Delgan/loguru) for more details.

## Misc

## Redoc

## Time
