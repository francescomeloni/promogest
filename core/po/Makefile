PREFIX=.
INSTALL= /usr/bin/install -c
INSTALL_PROGRAM= ${INSTALL}
INSTALL_DATA= ${INSTALL} -m 644
INSTALLNLSDIR=$(DESTDIR)/locale
top_srcdir = "."

MSGMERGE = intltool-update -x --gettext-package=$(NLSPACKAGE) --dist

NLSPACKAGE = promogest

CATALOGS = $(shell ls *.po)
FMTCATALOGS = $(patsubst %.po,%.mo,$(CATALOGS))

PYFILES  = $(wildcard ../promogest/ui/*.py) \
 $(wildcard ../promogest/ui/anag*/*.py) \
 $(wildcard ../promogest/ui/SimpleSearch/*.py) \
 $(wildcard ../promogest/ui/widgets/*.py) \
 $(wildcard ../promogest/modules/*/ui/*.py)

GLADEFILES = $(wildcard ../gui/*.glade) \
 $(wildcard ../promogest/modules/*/gui/*.glade)

TEMPLATEFILES = $(wildcard ../templates/*.html) \
 $(wildcard ../report-templates/*.html) \
 $(wildcard ../promogest/modules/*/templates/*.html) \
 $(wildcard ../promogest/modules/*/report-templates/*.html)

POTFILES  = $(PYFILES) $(GLADEFILES) $(TEMPLATEFILES)

all: $(NLSPACKAGE).pot $(FMTCATALOGS)

POTFILES.in:
	for file in $(POTFILES); do \
		echo "$${file#../}" ; \
	done > $@

$(NLSPACKAGE).pot: $(POTFILES) POTFILES.in
	intltool-update --gettext-package=$(NLSPACKAGE) --pot

update-po: Makefile $(NLSPACKAGE).pot refresh-po

refresh-po: Makefile POTFILES.in
	catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
		lang=`basename $$cat .po`; \
		cp $$lang.po $$lang.old.po; \
		if $(MSGMERGE) $$lang ; then \
			rm -f $$lang.old.po ; \
			echo "$(MSGMERGE) of $$lang succeeded" ; \
		else \
			echo "$(MSGMERGE) of $$lang failed" ; \
			mv $$lang.old.po $$lang.po ; \
		fi \
	done

report:
	@for cat in *.po ; do \
		echo -n "$$cat: "; \
		msgfmt --statistics -o /dev/null $$cat; \
	done

clean:
	@rm -fv *mo *~ .depend *.autosave

distclean: clean
	rm -f *mo .depend Makefile $(NLSPACKAGE).pot POTFILES.in

depend:

install:	all
	mkdir -p $(PREFIX)/$(INSTALLNLSDIR)
	for n in $(CATALOGS); do \
	    l=`basename $$n .po`; \
	    mo=$$l.mo; \
	    if [ ! -f $$mo ]; then continue; fi; \
	    $(INSTALL) -m 755 -d $(PREFIX)/$(INSTALLNLSDIR)/$$l; \
	    $(INSTALL) -m 755 -d $(PREFIX)/$(INSTALLNLSDIR)/$$l/LC_MESSAGES; \
	    $(INSTALL) -m 644 $$mo \
		$(PREFIX)/$(INSTALLNLSDIR)/$$l/LC_MESSAGES/$(NLSPACKAGE).mo; \
	done

%.mo: %.po
	msgfmt -o $@ $<
