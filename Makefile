ANSIBLE_DIR = ansible

.PHONY: deploy
deploy:
	ansible-playbook -i $(ANSIBLE_DIR)/hosts.yaml $(ANSIBLE_DIR)/deploy.yaml

.PHONY: setup
setup:
	ansible-playbook -i $(ANSIBLE_DIR)/hosts.yaml $(ANSIBLE_DIR)/setup.yaml
