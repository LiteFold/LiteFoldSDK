# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKeyListResponse", "APIKey"]


class APIKey(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    is_active: bool

    last_used_at: Optional[datetime] = None

    rate_limit_per_day: int

    rate_limit_per_hour: int


class APIKeyListResponse(BaseModel):
    api_keys: List[APIKey]
