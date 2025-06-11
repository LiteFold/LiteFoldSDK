# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    id: str

    created_at: datetime

    description: str

    key: str

    rate_limit_per_day: int

    rate_limit_per_hour: int
