CHECK=\033[32m✔\033[39m
DONE="\n$(CHECK) Done.\n"

SERVER=jcnrd.us
PROJECT=hackathon
PATH=deployment/$(PROJECT)
SUPERVISORCTL=/usr/bin/supervisorctl
SUCOPY=/bin/sucopy
SSH=/usr/bin/ssh
ECHO=/bin/echo -e
PIP=/usr/bin/pip
SUDO=/usr/bin/sudo
VENV=~/.virtualenvs/$(PROJECT)/bin/activate
ENTER_VENV=cd $(PATH); source $(VENV); pip install -r requirements.txt

.PHONY: remote_deploy depend configure supervisor nginx deploy compress clean collect run

run: collect
	@python manage.py runserver 0.0.0.0:8000

remote_deploy:
	@$(SSH) -t $(SERVER) "echo Deploy $(PROJECT) to the $(SERVER) server.; $(ENTER_VENV);  git pull; make deploy;"

depend:
	@$(ECHO) "\nInstall project dependencies..."

configure:
	@$(ECHO) "\nUpdate configuration..."
	@$(SUDO) $(SUCOPY) -r _deploy/etc/. /etc/.

supervisor:
	@$(ECHO) "\nUpdate supervisor configuration..."
	@$(SUDO) $(SUPERVISORCTL) reread
	@$(SUDO) $(SUPERVISORCTL) update
	@$(ECHO) "\nRestart $(PROJECT)..."
	@$(SUDO) $(SUPERVISORCTL) restart $(PROJECT)

nginx:
	@$(ECHO) "\nRestart nginx..."
	@$(SUDO) /etc/init.d/nginx restart

deploy: depend collect configure supervisor nginx
	@$(ECHO) $(DONE)

collect: compress
	@echo "\nCollecting static files..."
	@python manage.py collectstatic -i scripts -i styles -i Makefile --noinput
	@echo ${DONE}

compress:
	cd raw; make; cd ..

clean:
	@cd raw; make clean; cd ../..
