from invoke import task

@task
def build_proto(c):
    c.run(f"""poetry run python -m grpc_tools.protoc \
        -I=. \
        --grpc_python_out=. \
        --grpclib_python_out=. \
        --python_betterproto_out=. \
        proto/gisapp.proto""")
