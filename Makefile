.PHONY: compress

compress:
	@cd assets; make; cd ..

clean:
	cd assets; make clean; cd ../..
