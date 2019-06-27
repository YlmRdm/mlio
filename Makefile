.PHONY: all clean

STRACE_URL = "https://github.com/YlmRdm/mlio/blob/master/Exp2StraceBTIOckpt1n1.xlsx"

all: data/raw/Exp2StraceBTIOckpt1n1.xlsx

clean:
	rm -f data/raw/*.xlsx

data/raw/Exp2StraceBTIOckpt1n1.xlsx:
	python src/data/download.py $(STRACE_URL) $@
