test:
	python webim-test.py

clean:
	rm -f webim.pyc webim-test.pyc

push:
	bzr push lp:webim
