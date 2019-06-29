.PHONY: all clean test

# DATA_URL = "https://github.com/YlmRdm/mlio/blob/master/data/preprocessed/data.csv"

RAW_URL = "https://ylmrdm.github.io/download/Exp2StraceBTIOckpt1n1.xlsx"

all: data/raw/Exp2StraceBTIOckpt1n1.xlsx

clean:
	rm -f data/raw/*.xlsx

# data/preprocessed/data.csv:
# 	python src/data/download.py $(DATA_URL) $@

data/raw/Exp2StraceBTIOckpt1n1.xlsx:
	python src/data/download.py $(RAW_URL) $@

test: all
	pytest src
