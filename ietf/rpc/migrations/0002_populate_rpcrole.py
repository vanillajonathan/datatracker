# Generated by Django 4.2.4 on 2023-08-24 17:31

from django.db import migrations


def forward(apps, schema_editor):
    RpcRole = apps.get_model("rpc", "RpcRole")
    RpcRole.objects.create(slug="formatting", name="formatting", desc="Formatting an RFC")
    RpcRole.objects.create(slug="pe", name="primary editor", desc="First editor of an RFC")
    RpcRole.objects.create(slug="re", name="RFC editor", desc="Second editor of an RFC")
    RpcRole.objects.create(slug="finrev", name="FinRev", desc="Performs final checks after AUTH48")
    RpcRole.objects.create(slug="pub", name="PUB", desc="Publishes RFC")
    RpcRole.objects.create(slug="manager", name="manager", desc="RPC Manager")


def reverse(apps, schema_editor):
    RpcRole = apps.get_model("rpc", "RpcRole")
    RpcRole.objects.filter(
        slug__in=["formatting", "pe", "re", "finrev", "pub", "manager"]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("rpc", "0001_initial"),
    ]

    operations = [migrations.RunPython(forward, reverse)]
