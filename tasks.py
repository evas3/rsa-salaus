from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)

@task
def tests(ctx):
    ctx.run("pytest src", pty=True)
