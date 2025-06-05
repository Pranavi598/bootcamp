# 📘 Metadata Schema Design

This document outlines the **Metadata Schema Design** for storing detailed and extensible metadata extracted from a wide variety of file types. It supports structured, unstructured, and domain-specific data formats.

---

## 🔹 General Structure

```json
{
  "uuid": "unique_identifier_for_this_metadata_entry",
  "schema_version": "1.0"
}
```

---

## 📁 File System Metadata

```json
"file_system_metadata": {
  "file_path": "/path/to/your/file/example.bim",
  "extension": ".bim",
  "directory": "/path/to/your/file/",
  "size_bytes": 1234567,
  "creation_time_utc": "2024-06-05T08:30:00Z",
  "modification_time_utc": "2024-06-05T09:15:30Z",
  "last_access_time_utc": "2024-06-05T10:00:00Z",
  "owner_user": "john.doe",
  "owner_group": "data_analysts"
}
```

---

## 🔐 Checksums

```json
"checksums": {
  "md5": "a1b2c3d4e5f67890abcdef1234567890",
  "sha256": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
}
```

---

## 📄 General Content Metadata

```json
"general_content_metadata": {
  "is_binary": false,
  "is_text": true,
  "estimated_encoding": "UTF-8",
  "line_count": 1000,
  "character_count": 50000,
  "first_n_lines_sample": [
    "header_row_1,header_row_2",
    "data_row_1,data_row_2"
  ],
  "last_n_lines_sample": [],
  "inferred_delimiter": ",",
  "contains_keywords": [
    "chromosome",
    "gene",
    "variant"
  ]
}
```

---

## 🧬 Format-Specific Metadata

### 1. **PLINK `.bim` Files**

```json
"plink_bim": {
  "num_snps": 100000,
  "num_unique_chromosomes": 23,
  "chromosome_list": ["1", "2", "X", "Y"],
  "min_bp_position": 1000,
  "max_bp_position": 200000000,
  "average_genetic_distance": 0.5,
  "snp_id_prefix_distribution": {"rs": 0.9, "chr": 0.1}
}
```

---

### 2. **PLINK `.fam` Files**

```json
"plink_fam": {
  "num_individuals": 500,
  "num_unique_families": 100,
  "sex_distribution": {"1": 0.52, "2": 0.48},
  "phenotype_summary": {
    "disease_status": {"case": 0.3, "control": 0.7},
    "quantitative_trait_1": {
      "mean": 10.5,
      "std_dev": 2.1,
      "min": 5,
      "max": 15
    }
  },
  "contains_parents": true
}
```

---

### 3. **PLINK `.bed` Files**

```json
"plink_bed": {
  "num_samples": 500,
  "num_variants": 100000,
  "plink_bed_version": "v1.0",
  "magic_number_present": true
}
```

---

### 4. **Phenotype `.phen` Files**

```json
"phenotype_data": {
  "num_individuals": 450,
  "num_phenotypes": 3,
  "phenotype_names": ["Age", "BMI", "DiseaseStatus"],
  "phenotype_details": [
    {"name": "Age", "type": "numeric", "mean": 45.2, "std_dev": 12.3, "has_missing_values": false},
    {"name": "BMI", "type": "numeric", "mean": 25.1, "std_dev": 3.0, "has_missing_values": true},
    {"name": "DiseaseStatus", "type": "categorical", "unique_values": ["Healthy", "Affected"], "has_missing_values": false}
  ]
}
```

---

### 5. **Generic Text Files (`.txt`, `.csv`, `.log`)**

```json
"generic_text": {
  "line_ending_style": "LF",
  "has_header_row": true,
  "number_of_columns": 5,
  "potential_data_types_per_column": ["string", "integer", "float"],
  "comment_line_count": 10,
  "most_common_words": ["data", "sample", "result"]
}
```

---

### 6. **PDF Files**

```json
"pdf": {
  "num_pages": 10,
  "author": "Jane Doe",
  "creation_date": "2023-01-15T12:00:00Z",
  "is_encrypted": false,
  "has_attachments": true,
  "text_extract_sample": "First few sentences of extracted text for quick view..."
}
```

---


## 💡 Notes

- This schema is extensible to support additional file types or domains.
- All timestamps follow **ISO 8601** format in **UTC**.
- The `format_specific_metadata` field is a flexible container for domain-specific extractions.


## 🧪 Sample Use Cases

- Indexing metadata for large genomics datasets.
- Extracting quick previews for structured/unstructured files.
- Verifying file integrity using checksums.
