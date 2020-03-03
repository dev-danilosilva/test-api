from starlette.routing import Route, Mount
from src.controllers.note import get_all_notes, NoteByIdController, store

routes = [
    Mount('/api', routes=[
        Mount('/note', routes=[
            Route('/', get_all_notes, methods=['GET']),
            Route('/', store, methods=['POST']),
            Route('/{id}', NoteByIdController)
        ])
    ])
]
