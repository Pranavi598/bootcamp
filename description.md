# 📄 Meta-Indexer: Description Support in Uploads

This module supports adding human-readable **descriptions** (short or long) when uploading files. Descriptions are stored as part of the file’s metadata and help with later retrieval, documentation, and search.

---

## 🟢 Option 1: Add `--description` flag (inline)

Use this if your description is short and can be written directly in the terminal.

```bash
meta-indexer upload file.pdf --tags "domain=AI" --description "This paper explains the fundamentals of LLMs and transformers."
```

This uploads the file and stores a short description in the metadata.

---

## 🟡 Option 2: Pass description via a text file (for big descriptions)

Use this if your description is long or multi-line. Store it in a separate file and use `--description-file`.

```bash
meta-indexer upload file.pdf --tags "domain=AI" --description-file notes.txt
```

**Example: `notes.txt` content**
```txt
This is a comprehensive research paper explaining large language models (LLMs), their attention mechanisms, use in transformers, and their implications on natural language processing...
```

---

## 📦 Metadata Schema Update

A new top-level field `"description"` is added to your metadata schema as shown below:

```json
{
  "uuid": "unique_identifier_for_this_metadata_entry",
  "schema_version": "1.0",
  ...
  "description": "This paper explains the fundamentals of LLMs and transformers.",
  ...
}
```

For large descriptions:
```json
{
  ...
  "description": "This is a comprehensive research paper explaining large language models (LLMs), their attention mechanisms, use in transformers, and their implications on natural language processing...",
  ...
}
```

---

## 💡 Use Cases

- Explain what the file is about
- Include author notes or context
- Help others understand the content without opening the file
- Improve search accuracy

---

## ✅ Summary Table

| Feature                  | CLI Command Example                                                                       | Result in Metadata               |
|--------------------------|-------------------------------------------------------------------------------------------|----------------------------------|
| Short Description Inline | `--description "LLM overview"`                                                            | `"description": "LLM overview"`  |
| Long Description via File| `--description-file notes.txt`                                                            | `"description": "<file content>"`|

---

Feel free to integrate this into your CLI tool help docs or developer guide.
