# 📁 File Listing & Metadata Commands (Linux)

This document explains how to list files and directories across a server using standard Linux commands (`ls`, `find`, `stat`) and how to retrieve metadata about each file.

---

## 📂 Listing Files in the Server (or Specific Directory)

This uses the `ls` and `find` commands.

### ▶️ List files in the current directory

```bash
ls
```

---

### 🧾 List files with details (permissions, owner, size, date)

```bash
ls -l
```

---

### 👀 List all files including hidden ones (starting with `.`)

```bash
ls -a
```

---

### 📦 List files recursively from the current directory (shows all files and subdirectories)

```bash
ls -R
```

---

### 🔎 List all **regular files** from a specific path

(similar to `findcontent`'s initial step)

```bash
find /path/to/directory -type f
```

---

### 🗂️ List all files and directories recursively from a specific path

```bash
find /path/to/directory
```

---

### ⏱️ List files sorted by modification time (newest first)

```bash
ls -lt
```

---

## 🧾 Displaying File Metadata

This involves commands that show information about **files themselves**, not their content.

```bash
stat /path/to/your/file.txt
```

---
