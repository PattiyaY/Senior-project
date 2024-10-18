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
        authen = Custom("NextAuth.js", "./nextauthjs.png")
        manageUser = Gitlab("GitLab")
        frontend - authen
        frontend - manageUser

    with Cluster("Backend"):
        backend = MongoDB("MongoDB")
        queue = RabbitMQ("RabbitMQ")
        infra = Terraform("Terraform")
        cloud = AutomanagedVM("Azure VM")

    user >> frontend
    frontend >> queue
    queue >> frontend
    queue >> infra
    queue >> backend
    infra >> cloud
