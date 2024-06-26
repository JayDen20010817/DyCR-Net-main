

def get_tokenizer_roberta(results,opt):
    from transformers import RobertaTokenizer
    results["tokenizer_roberta"]=RobertaTokenizer.from_pretrained("DyCR-Net-main/roberta-base")

def get_tokenizer_bert(results,opt):
    from transformers import BertTokenizer
    results["tokenizer_bert"]=BertTokenizer.from_pretrained("DyCR-Net-main/roberta-base")

