.PHONY: fasttext

-include makefile.inc


sent2vec:
	git submodules init
	git submodules pull


sent2vec/fasttext: sent2vec
	$(MAKE) -C sent2vec clean
	$(MAKE) -C sent2vec


wheel: sent2vec/fasttext
	pip3 wheel --wheel-dir=./wheels .
