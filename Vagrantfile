# -*- mode: ruby -*-
# vi: set ft=ruby:fdm=marker

# Options {{{
#
APP_HOST = "33.33.33.2"
APP_HOSTNAME = "project.local"

MOUNT_DIR = "/usr/lib/project/source"
ANSIBLE_ROOT = "deploy"

# }}}


# Vagrant 2.0.x {{{
#
Vagrant.configure("2") do |config|
 
    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "precise64"
    # If your connection is slow download image manualy and run 'vagrant box add ...'
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    # Set hostname
    config.vm.hostname = APP_HOSTNAME

    # Configure network
    config.vm.network :private_network, ip: APP_HOST

    # Configure provider
    config.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      vb.customize ["modifyvm", :id, "--name", APP_HOSTNAME]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end

    # Share folder
    # config.vm.synced_folder '.', MOUNT_DIR, :nfs => true

    config.ssh.forward_agent = true

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = ANSIBLE_ROOT + "/playbook.yml"
        ansible.inventory_path = ANSIBLE_ROOT + "/inventory.ini"
        ansible.verbose = "vv"
        # ansible.tags = "wsgi"
        ansible.limit = 'vagrant'
    end

end
# }}}
