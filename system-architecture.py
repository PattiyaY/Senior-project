from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.onprem.database import MongoDB
from diagrams.onprem.queue import RabbitMQ
from diagrams.azure.compute import AutomanagedVM

with Diagram("IDP System Architecture", show=False):
    # User actor
    user1 = Custom("Developer", "./user.png")
    user2 = Custom("Project Manager", "./user.png")
    user3 = Custom("IT", "./user.png")

    # Frontend cluster (Next.js deployed on Vercel)
    with Cluster("Vercel"):
        frontend = Custom("NextJS", "./nextjs.png")
    
    # Backend cluster with MongoDB and RabbitMQ
    with Cluster("Database"):
        database = MongoDB("MongoDB")
    
    # Azure cloud cluster containing Azure VM
    with Cluster("Azure Cloud"):
        azure_vm = AutomanagedVM("Azure VM")
    
    # User interaction with the frontend
    user1 >> frontend
    user2 >> frontend
    user3 >> frontend

    # Frontend interacts with the database
    frontend >> database

    # Queue triggers interaction with Azure VM
    frontend >> azure_vm
