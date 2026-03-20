from transformers import pipeline
def init(model):
    global classifier
    if model == "multilingual-MiniLMv2-L6-mnli-xnli (speed)":
        print("loading multilingual-MiniLMv2-L6-mnli-xnli")
        classifier = pipeline("zero-shot-classification", model="MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli")
        
    
    elif model == "xlm-roberta-large-xnli (accuracy)":
        print("loading joeddav/xlm-roberta-large-xnli")
        classifier = pipeline("zero-shot-classification", model = "joeddav/xlm-roberta-large-xnli")
        

    else:
        print("loading MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
        classifier = pipeline("zero-shot-classification", model= "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
        

# Tag Where The File Should Be
def classify(content, Folders): # Learned The General Way Of This Function From Chatgpt
    return(classifier(content, Folders))