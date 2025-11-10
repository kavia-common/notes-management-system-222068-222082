# notes-management-system-222068-222082

## Backend (Django REST API)

Base URL for running container (preview): visit /docs for Swagger UI if enabled by the environment.

### Endpoints
- GET /api/health/ — health check
- Notes CRUD (JSON):
  - GET /api/notes/ — list notes
  - POST /api/notes/ — create note
  - GET /api/notes/{id}/ — retrieve single note
  - PUT /api/notes/{id}/ — update note
  - PATCH /api/notes/{id}/ — partial update note
  - DELETE /api/notes/{id}/ — delete note

Note: Routes are included under /api/ by the project’s root urls. If your environment expects /notes/ without /api/, adjust include path accordingly.

### Model
- Note: id (auto), title (string, required, max 200), content (text, optional), created_at, updated_at

### Run migrations
From notes_backend directory:
```bash
python manage.py migrate
```

### Seed sample data (optional)
```bash
python manage.py seed_notes
```

### Create a note example
```bash
curl -X POST http://localhost:3001/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Sample","content":"Hello"}'
```

### Security and best practices
- Input validated: title required and trimmed.
- CORS is enabled for local development (do not leave permissive in production).
- OWASP basics: use parameterized queries (Django ORM), avoid echoing untrusted data, use DEBUG=False in production, and rotate SECRET_KEY.

Reviewed & Approved by Engineering.