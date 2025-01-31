# Legal-Document# Legal Document Processing System

A Python-based NLP system for analyzing legal documents, extracting key clauses, and identifying important legal terms. This system uses state-of-the-art NLP techniques to process and analyze legal documents efficiently.

## Features

- 🔍 **Clause Extraction**: Automatically identify and extract key legal clauses (termination, liability, confidentiality)
- 📊 **Term Frequency Analysis**: Analyze and rank the most frequent legal terms across multiple documents
- 📑 **Document Insights**: Generate comprehensive document summaries and statistics
- ⚡ **Optimized Performance**: Parallel processing for handling large datasets
- 🔒 **Legal Term Focus**: Specialized processing for legal terminology

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/legal-document-processor.git
cd legal-document-processor
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download the required spaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Requirements

- Python 3.8+
- spaCy
- scikit-learn
- pandas
- numpy

See `requirements.txt` for complete dependencies.

## Usage

### Basic Usage

```python
from legal_document_processor import LegalDocumentProcessor

# Initialize the processor
processor = LegalDocumentProcessor()

# Process a single document
document = """
This Agreement may be terminated by either party upon 30 days written notice.
The Company shall not be liable for any indirect, special, or consequential damages.
All confidential information shall be kept strictly confidential for a period of 5 years.
"""

# Extract clauses
clauses = processor.extract_clauses(document)
print(clauses)

# Get document insights
insights = processor.get_document_insights(document)
print(insights)
```

### Processing Multiple Documents

```python
# Analyze multiple documents
documents = [doc1, doc2, doc3]  # List of document strings
frequent_terms = processor.analyze_term_frequency(documents, top_n=10)
print("Most Frequent Legal Terms:", frequent_terms)
```

## API Reference

### LegalDocumentProcessor

#### `extract_clauses(document: str) -> Dict[str, List[str]]`
Extracts key legal clauses from a document.

Parameters:
- `document` (str): Legal document text

Returns:
- Dictionary mapping clause types to lists of extracted clauses

#### `analyze_term_frequency(documents: List[str], top_n: int = 10) -> List[Tuple[str, int]]`
Analyzes frequency of legal terms across multiple documents.

Parameters:
- `documents` (List[str]): List of legal document texts
- `top_n` (int): Number of top terms to return (default: 10)

Returns:
- List of tuples containing (term, frequency)

#### `get_document_insights(document: str) -> Dict`
Generates comprehensive insights from a legal document.

Parameters:
- `document` (str): Legal document text

Returns:
- Dictionary containing document summary, key clauses, and statistics

## Performance Optimization

The system includes several optimizations:
- Parallel processing for multiple documents
- Efficient data structures
- Caching of spaCy models
- Memory-efficient processing

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- SpaCy for providing excellent NLP tools
- The legal NLP research community for insights and best practices

## Contact

Your Name - Saurabh Verma  saurabhvrm959@gmail.com


## To-Do

- [ ] Add support for more clause types
- [ ] Implement advanced document summarization
- [ ] Add unit tests
- [ ] Improve performance for very large documents
- [ ] Add support for different languages
