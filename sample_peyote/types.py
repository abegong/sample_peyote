from pydantic import BaseModel
from slugify import slugify

class DatasetIdea(BaseModel):
    name : str
    about : str
    use_cases :str

    @property
    def slug(self) -> str:
        return slugify(self.name)

class Table(BaseModel):
    name : str
    description: str
    columns: str

    @property
    def slug(self) -> str:
        return slugify(self.name)

class Sample(BaseModel):
    table_name : str
    csv : str