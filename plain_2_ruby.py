import re

input_txt = "彼は 政界[せいかい]なのに 有名人[ゆうめいじん]と<b>親[した]しい。</b>"
split_txt = [e for e in re.split(r'\s+|(\w+\[\w+\])|(\w+)|(<b>.*</b>)', input_txt) if e != '' and e is not None]
print(split_txt)
