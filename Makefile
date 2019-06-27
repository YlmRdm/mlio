.PHONY: all clean

DATA_URL = "https://github.com/YlmRdm/mlio/blob/master/data.csv"

all: data/raw/data.csv

clean:
	rm -f data/raw/*.csv

data/raw/Exp2StraceBTIOckpt1n1.xlsx:
	python src/data/download.py $(DATA_URL) $@
