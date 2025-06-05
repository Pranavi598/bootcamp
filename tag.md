# 🏷️ meta-indexer: Advanced Tagging Support in CLI

The `--tags` functionality in `meta-indexer` allows users to associate rich metadata with files at upload time. These tags help organize, search, and filter files in a structured and intelligent way.

---

## 🔍 Why Use Tags?

Tags help users:

- Quickly identify or categorize files
- Store useful metadata like domain, source, and quality
- Perform type-based filtering (e.g., all PDFs, all peer-reviewed files)
- Power downstream search, dashboards, and APIs

---

## 🛠️ Usage: `--tags` Options in CLI

```bash
meta-indexer upload file.pdf --tags "..."
```

---

## ✅ Tagging Formats You Can Use

### 🟢 1. Simple Topic Tags (Strings Only)

```bash
--tags "AI, LLM, transformers"
```

✔️ Great for general categorization  
🚫 Not structured — can't store values or types

Internally parsed as:
```json
["AI", "LLM", "transformers"]
```

---

### 🟡 2. Key=Value Pairs (Type Inferred Automatically)

```bash
--tags "domain=AI, reviewed=true, citations=23, score=8.75"
```

✔️ Best balance of simplicity and structure  
✔️ Supports string, boolean, integer, and float

Internally parsed as:
```json
{
  "domain": "AI",
  "reviewed": true,
  "citations": 23,
  "score": 8.75
}
```

---

### 🟠 3. Key:Type=Value (Strong Typing)

```bash
--tags "reviewed:bool=false, score:float=9.3, citations:int=100"
```

✔️ Ensures correct data types  
✔️ Ideal for validation and analytics

Internally parsed as:
```json
{
  "reviewed": false,
  "score": 9.3,
  "citations": 100
}
```

---

### 🔵 4. JSON Metadata File (Full Control)

```bash
--tags-file ./tags.json
```

`tags.json`:
```json
{
  "domain": "AI",
  "topics": ["LLM", "transformers"],
  "citations": 87,
  "peer_reviewed": true,
  "score": 9.2
}
```

✔️ Best for complex or nested metadata  
✔️ Programmatic and readable  
✔️ Supports lists, booleans, numbers, strings

---

### 🟣 5. Multiple `--tag` Flags (Granular CLI Control)

```bash
--tag domain=AI --tag reviewed=true --tag score=9.5
```

✔️ Easy to script in shell pipelines  
✔️ Familiar for users of Docker, Git, etc.

---

## 🧠 Supported Data Types in Tags

| Type      | Example Value              | Use Case                        |
|-----------|----------------------------|----------------------------------|
| `string`  | `"AI"`                     | Topic, domain, author           |
| `bool`    | `true`, `false`            | Reviewed status, flag toggles   |
| `int`     | `42`, `123`                | Citations, count, page number   |
| `float`   | `0.98`, `9.2`              | Quality scores, match %         |
| `list`    | `["AI", "LLM"]`            | Keywords, topics                |
| `date`    | `"2023-01-01T12:00:00Z"`   | Upload date, publish date       |
| `enum`    | `"status=draft/final"`     | Status tracking, type fields    |

---

## 📦 Metadata Schema (Example)

Here's how tags are embedded into file metadata in your backend:

```json
{
  "uuid": "abc123",
  "filename": "file.pdf",
  "uploaded_at": "2024-06-01T10:00:00Z",
  "tags": {
    "domain": "AI",
    "score": 8.75,
    "peer_reviewed": true,
    "citations": 100,
    "topics": ["LLM", "transformers"]
  }
}
```

---

## 📋 Real-World Examples

### Upload a PDF with topic tags:
```bash
meta-indexer upload paper.pdf --tags "AI, LLM, NLP"
```

### Upload with structured metadata:
```bash
meta-indexer upload report.pdf --tags "domain=finance, reviewed=true, score=9.0"
```

### Upload using strict types:
```bash
meta-indexer upload file.pdf --tags "domain:string=genomics, citations:int=900"
```

### Upload using external metadata file:
```bash
meta-indexer upload paper.pdf --tags-file meta_tags.json
```

---

---

## ✅ Summary Table

| Format           | Description                          | Example                                      |
|------------------|--------------------------------------|----------------------------------------------|
| Simple strings   | General topics                       | `"AI, transformers"`                         |
| Key=Value        | Structured tags                      | `"score=9.2, reviewed=true"`                 |
| Key:Type=Value   | Strongly typed                       | `"score:float=9.2"`                          |
| JSON file        | Complex or nested metadata           | `--tags-file tags.json`                      |
| Multiple `--tag` | CLI-friendly scripting               | `--tag domain=AI --tag score=9.5`            |

---

Let us know if you'd like to add tagging validation, autocomplete, or tag-based search features in future updates!
