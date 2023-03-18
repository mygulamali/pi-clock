ANSIBLE_DIR = ansible

.PHONY: setup
setup:
	ansible-playbook -i $(ANSIBLE_DIR)/hosts.yaml $(ANSIBLE_DIR)/setup.yaml
