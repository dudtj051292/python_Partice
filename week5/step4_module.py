from re import sub


st3 = 'test^홍길동 abc 대한*민국 123$tbc'
text1 = sub('[\^*$]+','', st3)
print(text1)
text2 = sub('[0-9]','', text1)
print(text2)

texts = ['우리나라 땡땡  대한민국, 우리나라%$ 만세', '헐 보험료 15000원에  헐 평생 보장 마감 임박', '헐땡땡 나는 홍길동']
print(texts[0])
not_allow = ['땡땡', '헐']
def clean_text(text_string) :
    clean_text = sub('[\^*#%@$]+', '',  text_string) # 특문
    clean_text = sub('[0-9]+', '',  clean_text) # 숫자
    clean_text = clean_text.upper() # 숫자
    #비속어 제거
    clean_text = sub()
    return clean_text

for txt in texts :
    print(clean_text(txt))


