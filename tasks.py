from invoke import task


@task
def portrait(c):
    c.run('python main.py -m screen:droid2,scale=.75,portrait -m inspector')


@task
def landscape(c):
    c.run('python main.py -m screen:droid2,landscape -m inspector')


@task
def unittest(c):
    c.run('python -m unittest')


@task
def docker_build(c):
    c.run('docker build --tag=buildozer .')


@task
def docker_run(c):
    c.run('docker run --volume "$(pwd)":/home/user/hostcwd buildozer --version')