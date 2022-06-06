import pycorrector
from hanlp_restful import HanLPClient
HanLP = HanLPClient('https://www.hanlp.com/api', auth=None, language='zh')

sent = input()
simplified_sentence = pycorrector.traditional2simplified(sent)
precorr_sent, err = pycorrector.correct(simplified_sentence)
print(precorr_sent)
key = HanLP.keyphrase_extraction(precorr_sent)
print(key.keys())
print(HanLP(precorr_sent, tasks='tok/coarse'))
