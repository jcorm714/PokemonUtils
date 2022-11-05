from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import logging
from services.PokemonDraftGenerator import PokemonDraftGenerator
from services.PokemonDraftGeneratorOptions import PokemonDraftGeneratorOptions


#import startup task script
import startup

logging.basicConfig(format="[%(asctime)s %(levelname)s %(filename)s]: %(message)s", filename="app.log")
app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/pokeutils/draft")
async def generate_draft_csv(options: PokemonDraftGeneratorOptions):
        draft_generator = PokemonDraftGenerator()
        draft_generator.set_service_options(options)
        draft_generator.handle_request()
        
        response = StreamingResponse(iter([draft_generator.service_output.getvalue()]))
        response.headers["Content-Disposition"] = "attachment; filename=draft.csv"
        return response

