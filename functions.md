
---

## 🔍 How to Use the `search_content` Function

### 🚫 Without LLM

```bash
sudo findcontent / chromosome gene protein
```

We can search for the files using **GREP** and **strings** functions:

```bash
find /path/to/your/server/data/ -type f -print0 | while IFS= read -r -d $'\0' file; do
    # Use -f to read patterns from a file
    if grep -q -i -f keywords.txt "$file"; then
        echo "Found in (grep): $file"
    else
        # If grep doesn't find it, try strings + grep for binary/mixed files
        if strings "$file" | grep -q -i -f keywords.txt; then
            echo "Found in (strings + grep): $file"
        fi
    fi
done
```

We integrate the above functionality into the module itself.

So from the user’s terminal:

```bash
# If you suspect the keywords might be in user home directories:
sudo findcontent /home/ chromosome gene protein

# If you suspect they might be in an application's data directory:
sudo findcontent /opt/my_app/data/ chromosome gene protein
```

---
### 🤖 With LLM

Search files using intelligent context-aware processing (backed by LLM logic).

To search for specific keywords in a particular directory:

```bash
search_files /home/myuser/documents "report" "sales" "quarterly"
```

This internally calls your backend Python script which executes the `findcontent` logic.

To search for a single keyword in a log directory:

```bash
search_files /var/log "error"
```

To search the entire server (requires sudo and will be slow):

```bash
sudo search_files / "configuration" "database"
meta-indexer upload file.txt --tags "category=genomics" "owner=john.doe" "confidence=0.92"
```
