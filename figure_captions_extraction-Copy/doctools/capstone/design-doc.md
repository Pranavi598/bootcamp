
---

### ✅ `capstone/design-doc.md`

```markdown
# 🛠️ Design Document – Real-Time File Processing System

## 📌 Problem

We need a system to monitor a folder for incoming files, process them line-by-line, and expose internal state via FastAPI.

## 🎯 Goals

- Modular stream processing
- File monitoring
- FastAPI metrics dashboard

## 🚫 Non-Goals

- Distributed processing
- Complex UIs

## ✅ Decision

Python + Watchdog + FastAPI. Simple, extensible, and works well locally or in Docker.

## ⚠️ Risks

- File watcher delays
- Stream stalls
