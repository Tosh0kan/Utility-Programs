import re

input_txt = "彼は 政界[せいかい]なのに 有名人[ゆうめいじん]と<b>親[した]しい。</b>"

first_split = input_txt.split(' ')
second_split = []

for e in first_split:
    if ']' in e:
        if e[-1] != ']':
            chunk = []
            if e[-2] != ']':
                for i in reversed(e):
                    if i != ']':
                        chunk.append(i)
                    elif i == ']':
                        rev_chunk_str = ''.join([kana for kana in reversed(chunk)])
                        second_split.append(e.replace(rev_chunk_str, ''))
                        second_split.append(rev_chunk_str)
            else:
                second_split.append(e[0:-1])
                second_split.append(e[-1])
        else:
            second_split.append(e)
    else:
        second_split.append(e)


