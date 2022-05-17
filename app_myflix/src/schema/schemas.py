from pydantic import BaseModel
from typing	import Optional

class Series(BaseModel):

    id: Optional[int] = None
    titulo: str
    ano: int
    genero: str
    qtd_temporadas: int

    class config:
        orm_mode = True