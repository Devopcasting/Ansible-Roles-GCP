import functions_framework

@functions_framework.http
def hello(request):
    return "Ansible: GCP Cloud Function"
