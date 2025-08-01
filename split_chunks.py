from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_into_chunks(text, chunk_size = 500, overlap = 100):

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)

    return splitter.split_text(text)

