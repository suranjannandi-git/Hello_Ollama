import fitz  # PyMuPDF
import call_ollama as ollama

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text("text")
    pdf_document.close()
    return text

def summarize_text(text):
    prompt = f"""Summarize the below text in not more than 50 words. 
    {text}
    """

    response = ollama.get_ollama_chat_response(prompt)
    for chunk in response:
        print(chunk["message"]["content"], end='', flush=True)


if __name__ == "__main__":
    text = extract_text_from_pdf("sample_file/index.pdf")
    summarize_text(text)