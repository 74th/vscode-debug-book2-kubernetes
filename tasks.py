from invoke import task

@task
def build_proto(c):
    c.run(f"""poetry run python -m grpc_tools.protoc \
        -I=. \
        --python_betterproto_out=. \
        proto/gisapp.proto""")

@task
def build_default_proto(c):
    c.run(f"""protoc -I=. --python_out=. ./proto/gisapp.proto""")

@task
def apply_base(c):
    c.run(f"""kustomize build manifests/base | kubectl apply -f -""")

@task
def apply_cloudcode(c):
    c.run(f"""kustomize build manifests/cloudcode | kubectl apply -f -""")

@task
def apply_debugpy(c):
    c.run(f"""kustomize build manifests/debugpy | kubectl apply -f -""")
