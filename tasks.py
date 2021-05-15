from invoke import task

@task
def build_proto(c):
    c.run(f"""poetry run python -m grpc_tools.protoc \
        -I=. \
        --python_betterproto_out=. \
        proto/gisapp.proto""")

@task
def apply(c):
    c.run(f"""kustomize build manifests/ | kubectl apply -f -""")
