MAIN_CLASS=io.jqb.App
CLASSPATH=$(shell python .class.path)
SOURCE=$(shell pwd)/src/main/java:$(shell pwd)/src/test/java


.PHONY: check-syntax


# Needed for emacs fly-make
check-syntax:
	javac -cp $(CLASSPATH) -Xlint $(CHK_SOURCES)


compile: clean
	mvn compile


start: compile
	@echo "============================================================"
	java -cp $(CLASSPATH) $(MAIN_CLASS) $(ARGS)


run:
	@echo "============================================================"
	java -cp $(CLASSPATH) $(MAIN_CLASS) $(ARGS)


clean:
	mvn clean
