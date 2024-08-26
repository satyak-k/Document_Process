import pytesseract
import spacy

from pdf2image import convert_from_path
from PIL import Image

from transformers import pipeline


def split_text(text, chunk_size=512):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def aggregate_results(results):
    aggregated_result = []
    for result in results:
        aggregated_result.extend(result)
    return aggregated_result

def text_analysis(text):
    nlp = spacy.load('en_core_web_sm')

    classifier = pipeline('text-classification', model='bert-base-uncased')
    sentiment_analyzer = pipeline('sentiment-analysis',
                                  model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')

    doc = nlp(text)
    named_entities = {ent.label_: ent.text for ent in doc.ents}

    split_texts = split_text(text, chunk_size=512)

    classification_results = [classifier(t) for t in split_texts]
    sentiment_results = [sentiment_analyzer(t) for t in split_texts]

    aggregated_classification = aggregate_results(classification_results)
    aggregated_sentiment = aggregate_results(sentiment_results)

    results = {
        'named_entities': named_entities,
        'text_classification': aggregated_classification,
        'sentiment_analysis': aggregated_sentiment
    }

    return results

def extract_text_from_pdf(pdf_path, poppler_path, lang='eng'):
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    extracted_text = ''

    for image in images:
        text = pytesseract.image_to_string(image, lang=lang)
        extracted_text += text + '\n'
    return extracted_text

def extract_text_from_image(image, lang='eng'):
    image = Image.open(image)
    text = pytesseract.image_to_string(image, lang=lang)
    return text
