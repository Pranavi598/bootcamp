# 🔄 Replacing a File's Content with a Local File (Upload & Overwrite)

This guide explains how to upload an updated version of a file from your local machine to a remote server, effectively overwriting the old version.

---

## Using `scp` (Secure Copy Protocol)

`scp` is a simple tool to securely copy files between local and remote systems.

> **Note:** `scp` will overwrite the existing file on the server **without asking for confirmation** if the file path and name are the same. Be careful to specify correct paths.

```bash
scp /path/to/local/updated_file.txt user@your_server_ip:/path/to/remote/existing_file.txt
```

---

## Using `rsync` (Recommended for efficiency and robustness)

`rsync` is preferred for syncing files, especially for large files or repeated updates because it only transfers the differences between local and remote files.

```bash
rsync -avz /path/to/local/updated_file.txt user@your_server_ip:/path/to/remote/existing_file.txt
```

---

