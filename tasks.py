from invoke import task

@task
def build_proto(c):
    module_path = "github.com/74th/vscode-debug-book2"
    with c.cd("proto"):
        c.run(f"""protoc\
            --go_out=. --go_opt=Mgisapp.proto={module_path} \
            --go-grpc_out=. --go-grpc_opt=Mgisapp.proto={module_path} \
            ./gisapp.proto""")