.PHONY: check-syntax

# Needed for emacs fly-make
check-syntax:
	javac -Xlint $(CHK_SOURCES)


compile: clean
	javac -cp . *.java


start: compile
	java Main


clean:
	find . -name "*.class" -exec rm {} \;
