# Litefold Python API library

[![PyPI version](<https://img.shields.io/pypi/v/litefold.svg?label=pypi%20(stable)>)](https://pypi.org/project/litefold/)

The Litefold Python library provides convenient access to the Litefold REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainless.com/).


## Installation

```sh
# install from PyPI
pip install --pre litefold
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from litefold import Litefold

client = Litefold(
    api_key=os.environ.get("LITEFOLD_API_KEY"),  # This is the default and can be omitted
)

response = client.upload.create_fasta(
    files=[b"raw file contents"],
    job_name="job_name",
)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `LITEFOLD_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

## Async usage

Simply import `AsyncLitefold` instead of `Litefold` and use `await` with each API call:

```python
import os
import asyncio
from litefold import AsyncLitefold

client = AsyncLitefold(
    api_key=os.environ.get("LITEFOLD_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    response = await client.upload.create_fasta(
        files=[b"raw file contents"],
        job_name="job_name",
    )


asyncio.run(main())
```

## Structure Prediction
Here is a simple example on how to run structure prediction for LiteFold

```python
import os
from litefold import Litefold

client = Litefold(
    api_key=os.environ.get("LITEFOLD_API_KEY"),  # This is the default and can be omitted
)
response = client.structure_prediction.submit(
    job_name="job_name",
    model_name="model_name",
)
print(response)
```


Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |



