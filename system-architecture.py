from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.onprem.vcs import Gitlab
from diagrams.onprem.database import MongoDB
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.iac import Terraform
from diagrams.azure.compute import AutomanagedVM


with Diagram("IDP System Architecture", show=False):
    user = Custom("User", "./user.png")

    with Cluster("Frontend"):
        frontend = Custom("NextJS", "./nextjs.png")

    with Cluster("Backend"):
        backend = MongoDB("MongoDB")
        queue = RabbitMQ("RabbitMQ")
        infra = Terraform("Terraform")
        cloud = AutomanagedVM("Azure VM")

        # GitLab is now part of the backend, used for code repository/CI, not for managing user permissions
        gitlab = Gitlab("GitLab")

    # NextAuth.js is considered part of the internal workings of NextJS, so it's not necessary to show explicitly in the architecture

    # User interaction with frontend
    user >> frontend

    # Frontend interaction with backend via message queue
    frontend >> queue
    queue >> frontend

    # Queue interacting with the backend services
    queue >> infra
    queue >> backend
    backend >> queue

    # Terraform managing Azure VM provisioning
    infra >> cloud

    # GitLab remains in the backend cluster for CI/CD or repository management
    gitlab >> infra
