from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
# import h5py

def analyzer(inp):
    # MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

    # example = "This oatmeal is not good. Its mushy, soft, I don't like it. Quaker Oats is the way to go."

    encoded_text = tokenizer(inp, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'neg' : scores[0],
        'neu' : scores[1],
        'pos' : scores[2]
    }

    return scores_dict

def result(inp):
    scores_dict = analyzer(inp)
    neg = scores_dict.get('neg')
    neu = scores_dict.get('neu')
    pos = scores_dict.get('pos')

    if(neg > neu):
        if(neg > pos):
            return "NEGATIVE"
        else:
            return "POSITIVE"
    else:
        if(neu > pos):
            return "NEUTRAL"
        else:
            return "POSITIVE"
