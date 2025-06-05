Certainly! Here’s a clean, easy-to-use **README.md** file for the REST API commands for your `meta-indexer` tool:

```markdown
# Meta-Indexer REST API Guide

This document describes the REST API endpoints for uploading files with tags and descriptions, updating metadata, searching, listing, downloading, and deleting files.

---

## 1. Upload a File with Tags and Description

### Endpoint
```

POST /upload

```

### Content-Type
```

multipart/form-data

````

### Request Fields

| Field       | Type           | Description                           |
| ----------- | -------------- | ----------------------------------- |
| `file`      | file (binary)  | File to upload                      |
| `tags`      | string or JSON | Tags, comma-separated or JSON format|
| `description`| string        | Optional description of the file    |

### Example: Upload with Inline Tags and Description

```bash
curl -X POST http://yourserver.com/upload \
  -F "file=@/home/user/research.pdf" \
  -F "tags=domain=AI,score=9.2,reviewed=true" \
  -F "description=This is a research paper on transformers."
````

### Example: Upload with Description File

```bash
curl -X POST http://yourserver.com/upload \
  -F "file=@/home/user/research.pdf" \
  -F "tags=domain=AI,score=9.2" \
  -F "description=@/home/user/desc.txt"
```

---

## 2. Update Tags or Description for an Existing File

### Endpoint

```
PUT /metadata/<file_id>
```

### Content-Type

```
application/json
```

### Example: Update Metadata

```bash
curl -X PUT http://yourserver.com/metadata/123 \
  -H "Content-Type: application/json" \
  -d '{
        "tags": {
          "domain": "AI",
          "citations": 120
        },
        "description": "Updated transformer model comparison"
      }'
```

---

## 3. Search Files by Content or Metadata

### Endpoint

```
GET /search
```

### Query Parameters

* `query`: keyword(s) to search inside files
* `tag`: filter by tags in `key:value` format (optional)

### Example

```bash
curl "http://yourserver.com/search?query=transformer&tag=domain:AI"
```

---

## 4. List All Files

### Endpoint

```
GET /files
```

### Example

```bash
curl http://yourserver.com/files
```

---

## 5. Download a File

### Endpoint

```
GET /files/<file_id>/download
```

### Example

```bash
curl -O http://yourserver.com/files/123/download
```

---

## 6. Delete a File

### Endpoint

```
DELETE /files/<file_id>
```

### Example

```bash
curl -X DELETE http://yourserver.com/files/123
```

---

## Backend Metadata Schema Example

```json
{
  "file_id": 123,
  "filename": "research.pdf",
  "tags": {
    "domain": "AI",
    "score": 9.2
  },
  "description": "This is a paper on transformers and LLMs",
  "upload_date": "2025-06-05T10:30:00Z"
}
```

---

Feel free to reach out if you want sample server implementations, Postman collections, or integration examples!

```

If you want, I can help generate the server code or Postman collection next!
```
