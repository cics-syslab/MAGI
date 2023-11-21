# PRIVATE_BEGIN
# Set semester and project info
SEMESTER = $(shell test -f scripts/semester.txt     && cat scripts/semester.txt)
ifeq ($(SEMESTER),)
$(error SEMESTER is not defined (please provide scripts/semester.txt))
else
$(info SEMESTER = $(SEMESTER))
endif

PROJNAME = $(shell test -f scripts/project-name.txt && cat scripts/project-name.txt)
ifeq ($(PROJNAME),)
$(error PROJNAME is not defined (please provide (non-empty) scripts/project-name.txt))
else
$(info PROJNAME = $(PROJNAME))
endif

EXECNAME = $(subst -,_,$(shell test -f scripts/project-name.txt && cat scripts/project-name.txt))
$(info EXECNAME = $(EXECNAME))
# PRIVATE_END
_DEPS = sum.h
_OBJ = sum.o
_MOBJ = main.o
_TOBJ = test.o

APPBIN = $(EXECNAME)_app
TESTBIN = $(EXECNAME)_test

IDIR = include
CC = gcc
CFLAGS = -I$(IDIR) -Wall -Wextra -g -pthread
ODIR = obj
SDIR = src
LDIR = lib
TDIR = test
LIBS = -lm
XXLIBS = $(LIBS) -lstdc++ -lgtest -lgtest_main -lpthread
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
MOBJ = $(patsubst %,$(ODIR)/%,$(_MOBJ))
TOBJ = $(patsubst %,$(ODIR)/%,$(_TOBJ))
SRC = $(wildcard $(SDIR)/*.c)

$(ODIR)/%.o: $(SDIR)/%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/%.o: $(TDIR)/%.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

all: app test sub

app: $(APPBIN)

test: $(TESTBIN)

sub: submission-$(PROJNAME).zip

$(APPBIN): $(MOBJ) $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

$(TESTBIN): $(TOBJ) $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(XXLIBS)

submission-$(PROJNAME).zip: $(SRC) $(DEPS)
	zip $@ $^

# PRIVATE_BEGIN
format:
	find ./src -regex '.*\.\(cpp\|hpp\|c\|h\)' -exec clang-format -style=file -i {} \;
	find ./test -regex '.*\.\(cpp\|hpp\|c\|h\)' -exec clang-format -style=file -i {} \;
	find ./include -regex '.*\.\(cpp\|hpp\|c\|h\)' -exec clang-format -style=file -i {} \;

dist: format
	@if ! [ -d docs/$(SEMESTER) ]; then \
	   echo "CREATING NEW DOCS SUBFOLDER FOR SEMESTER $(SEMESTER)"; \
	   mkdir -p docs/$(SEMESTER); \
	fi
	@if [ -f docs/$(SEMESTER)/index.md ]; then \
	   cp docs/$(SEMESTER)/index.md docs/$(SEMESTER)/index.md.save; \
	fi
	cp -p docs/master/index.md docs/$(SEMESTER)
	SEMESTER=$(SEMESTER) PROJNAME=$(PROJNAME) EXECNAME=$(EXECNAME) python3 scripts/distribute.py
	@if [ -f docs/$(SEMESTER)/index.md.save ]; then \
	   if ! diff -q docs/$(SEMESTER)/index.md docs/$(SEMESTER)/index.md.save > /dev/null; then \
	      echo "SAVING PREVIOUS docs/$(SEMESTER)/index.md"; \
	      mv docs/$(SEMESTER)/index.md.save docs/$(SEMESTER)/index.md-$$(stat --format=%Y docs/$(SEMESTER)/index.md.save); \
	   else \
	      rm docs/$(SEMESTER)/index.md.save; \
	   fi; \
	fi

publish: dist
	git add .
	git commit -am 'Update to distribution'

distclean: clean
	rm -rf dist
# PRIVATE_END

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~
	rm -f $(APPBIN) $(TESTBIN)
	rm -f submission-$(PROJNAME).zip
