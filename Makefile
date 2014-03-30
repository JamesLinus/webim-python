test:
	python webim_test.py

clean:
	rm -f webim.pyc webim_test.pyc

upload:
	python setup.py sdist upload
