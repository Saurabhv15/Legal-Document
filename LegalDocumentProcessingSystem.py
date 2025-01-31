import spacy
from collections import Counter
from typing import List, Dict, Tuple
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import numpy as np


nlp = spacy.load("en_core_web_sm")

class LegalDocumentProcessor:
    def __init__(self):
        self.legal_terms = set([
            "liability", "indemnification", "termination", "warranty",
            "confidentiality", "arbitration", "jurisdiction", "force majeure"
        ])
        self.tfidf = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 3),
            max_features=1000
        )
    
    def extract_clauses(self, document: str) -> Dict[str, List[str]]:
        """

        
        Args:
            document (str): Legal document text
            
        Returns:
            Dict[str, List[str]]: Dictionary of clause types and their content
        """
        clauses = {
            "termination": [],
            "liability": [],
            "confidentiality": []
        }
        

        doc = nlp(document)
        

        sentences = [sent.text.strip() for sent in doc.sents]
        

        patterns = {
            "termination": r"(?i)(terminat(e|ion)|cancel(lation)?).{0,200}",
            "liability": r"(?i)(liab(le|ility)|indemnif(y|ication)).{0,200}",
            "confidentiality": r"(?i)(confidential(ity)?|non-disclosure).{0,200}"
        }
        

        for clause_type, pattern in patterns.items():
            for sentence in sentences:
                if re.search(pattern, sentence):
                    clauses[clause_type].append(sentence)
        
        return clauses

    def analyze_term_frequency(self, documents: List[str], top_n: int = 10) -> List[Tuple[str, int]]:
        """

        
        Args:
            documents (List[str]): List of legal document texts
            top_n (int): Number of top terms to return
            
        Returns:
            List[Tuple[str, int]]: List of (term, frequency) tuples
        """

        with ProcessPoolExecutor() as executor:
            processed_docs = list(executor.map(self._process_single_doc, documents))
        

        all_terms = []
        for doc_terms in processed_docs:
            all_terms.extend(doc_terms)
        

        term_freq = Counter(all_terms)
        

        legal_term_freq = {term: freq for term, freq in term_freq.items() 
                          if any(legal_term in term.lower() for legal_term in self.legal_terms)}
        
        return sorted(legal_term_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def _process_single_doc(self, document: str) -> List[str]:
        """

        
        Args:
            document (str): Document text
            
        Returns:
            List[str]: List of legal terms found in the document
        """
        doc = nlp(document)
        terms = []
        
        # Extract noun phrases and filter for legal terms
        for chunk in doc.noun_chunks:
            if any(legal_term in chunk.text.lower() for legal_term in self.legal_terms):
                terms.append(chunk.text.lower())
        
        return terms

    def get_document_insights(self, document: str) -> Dict:
        """

        
        Args:
            document (str): Legal document text
            
        Returns:
            Dict: Dictionary containing various document insights
        """
        doc = nlp(document)
        
        insights = {
            'summary': self._generate_summary(doc),
            'key_clauses': self.extract_clauses(document),
            'document_stats': {
                'total_words': len(doc),
                'sentences': len(list(doc.sents)),
                'entities': self._extract_entities(doc)
            }
        }
        
        return insights
    
    def _generate_summary(self, doc) -> str:

        # Get important sentences based on noun phrase density
        important_sentences = []
        for sent in doc.sents:
            if len(list(sent.noun_chunks)) > 3:
                important_sentences.append(sent.text)
        
        return " ".join(important_sentences[:3])
    
    def _extract_entities(self, doc) -> Dict[str, List[str]]:

        entities = {}
        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []
            entities[ent.label_].append(ent.text)
        
        return entities


if __name__ == "__main__":
    processor = LegalDocumentProcessor()
    

    sample_doc = """
    This Agreement may be terminated by either party upon 30 days written notice.
    The Company shall not be liable for any indirect, special, or consequential damages.
    All confidential information shall be kept strictly confidential for a period of 5 years.
    """
    

    clauses = processor.extract_clauses(sample_doc)
    print("Extracted Clauses:", clauses)
    

    documents = [sample_doc] * 3  # Example with multiple copies of same doc
    frequent_terms = processor.analyze_term_frequency(documents)
    print("Most Frequent Legal Terms:", frequent_terms)
    

    insights = processor.get_document_insights(sample_doc)
    print("Document Insights:", insights)