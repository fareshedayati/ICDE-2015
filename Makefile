BUILD_DIR ?= build

PDF_READER ?= open
PDFLATEX ?= pdflatex -halt-on-error -shell-escape
BIBTEX ?= bibtex

all: clean article

article:
	$(PDFLATEX) ICDE.tex
	$(BIBTEX) ICDE
	$(PDFLATEX) ICDE.tex
	$(PDFLATEX) ICDE.tex

partial:
	$(PDFLATEX) ICDE.tex

view: build
	@$(PDF_READER) ICDE.pdf &

log:
	@open ICDE.log

.PHONY: clean

clean:
	rm -f *.log *.out *.aux *.bbl *.blg ICDE.pdf
