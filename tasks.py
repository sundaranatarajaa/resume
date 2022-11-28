from invoke import task


@task
def build(c,path):
    c.run(f"poetry run generate_resume {path}")
