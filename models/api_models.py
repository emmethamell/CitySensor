from pydantic import BaseModel
from typing import List, Optional

class MyModel(BaseModel):
    links: List[str]
    subtype: Optional[str] = None
    city: Optional[str] = None