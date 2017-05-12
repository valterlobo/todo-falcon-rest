from fabric.api import local


def prepare_deploy():
    local("git add -p && git commit" )

def remote():
     local("git push origin")
