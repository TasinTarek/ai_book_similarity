# AI Book Similarity - Odoo 19 Vector Demo

This module is a demonstration of the powerful new **AI Vector fields** introduced in **Odoo 19 Enterprise**. It showcases how to store high-dimensional embeddings and perform semantic similarity searches natively within the Odoo ORM.

## 🚀 Features

- **Semantic Storage**: Uses the new `Vector` field type to store 1536-dimensional embeddings.
- **Fast Search**: Implements the `IVFFlat` index for lightning-fast approximate nearest neighbor (ANN) searches.
- **Native SQL Integration**: Leverages the PostgreSQL `<=>` (cosine distance) operator for semantic comparisons.
- **Mock Demo Mode**: Includes a tool to generate mock vector data so you can test the similarity logic without needing an LLM API key.

## 📋 Prerequisites

To run this module, your environment must have:
1. **Odoo 19 Enterprise** (or Community with the `ai` base module).
2. **PostgreSQL 14+**.
3. **pgvector extension**: This must be installed in your PostgreSQL environment.
   ```bash
   # Quick install for macOS (Homebrew)
   brew install pgvector
   ```

## 🛠️ Installation

1. Copy the `ai_book_similarity` folder into your Odoo addons directory.
2. Restart your Odoo server.
3. Enable **Developer Mode** in Odoo.
4. Go to **Apps** -> **Update App List**.
5. Search for "AI Book Similarity" and click **Install**.

## 📖 How to Use

1. Navigate to the new **AI Book Similarity** menu.
2. Create several book records with varied descriptions (e.g., one about Space, one about Cooking, one about History).
3. On each book, click the **Generate Mock Vector** button. (This simulates an LLM generating an embedding for the description).
4. Once you have multiple books with vectors, click **Find Similar Books** on any record.
5. Odoo will perform a semantic search and return the top 5 most similar books based on their "meaning" rather than just keywords.

## 💻 Technical Implementation

### The Vector Field
```python
description_vector = Vector(size=1536)
```

### The Similarity Query
```python
SELECT id
FROM ai_example_book
ORDER BY description_vector <=> %s::vector
LIMIT 5
```

## 📜 License
LGPL-3
