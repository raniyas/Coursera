text = "X-DSPAM-Confidence:    0.8475"
num_pos = text.find(':')
num = float(text[num_pos+1 : ].strip())
print(num)