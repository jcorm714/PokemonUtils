from pydantic import BaseModel
class PokemonDraftGeneratorOptions(BaseModel):
        region: str
        exclude: str | None = None
        sample_size = 100
        replace_when_sample = False