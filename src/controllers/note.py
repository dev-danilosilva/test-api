from orm import NoMatch
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException

from src.models.note import Note


async def get_all_notes(request: Request):
    notes = await Note.objects.all()

    content = [
        {
            "id": note.id,
            "description": note.description,
            'status': note.status,
        }
        for note in notes
    ]
    return JSONResponse(content) if len(content) > 0 else JSONResponse({'message': 'empty'})


async def store(request: Request):
    note = await request.json()
    created = await Note.objects.create(
        description=note['description'],
        status=note['status']
    )

    content = {
        'id': created.id,
        'description': created.description,
        'status': created.status
    }

    return JSONResponse(content)


class NoteByIdController(HTTPEndpoint):
    async def get(self, request: Request):
        id = request.path_params['id']

        try:
            note = await Note.objects.get(id=id)
        except NoMatch as e:
            raise HTTPException(404, 'Resource Not Found')

        content = {
            'id': note.id,
            'description': note.description,
            'status': note.status
        }

        return JSONResponse(content)

    async def put(self, request: Request):
        pass

    async def delete(self, request: Request):
        pass
