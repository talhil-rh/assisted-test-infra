"""
kube_helpers package provides infra to deploy, manage and install cluster using
CRDs instead of restful API calls.

Use this package as part of pytest infra with the fixture kube_api_context.
It provides a KubeAPIContext object which holds information about the resources
created as well as the kubernetes ApiClient.

Example of usage:

def test_kube_api_wait_for_install(kube_api_context):
    kube_api_client = kube_api_context.api_client
    cluster_deployment = deploy_default_cluster_deployment(
        kube_api_client, 'test-cluster', **installation_params
    )
    cluster_deployment.wait_to_be_installing()

An Agent CRD will be created for each registered host. In order to start the
installation all agents must be approved.
When a ClusterDeployment has sufficient data and the assigned agents are
approved, installation will be started automatically.
"""

from .cluster_deployment import (
    deploy_default_cluster_deployment,
    Platform,
    InstallStrategy,
    ClusterDeployment
)
from .cluster_image_set import (
    ClusterImageSet,
    ClusterImageSetReference
)
from .agent import Agent
from .nmstate_config import NMStateConfig
from .secret import deploy_default_secret, Secret
from .infraenv import deploy_default_infraenv, InfraEnv, Proxy
from .common import (
    create_kube_api_client,
    delete_all_resources,
    suppress_not_found_error,
    UnexpectedStateError,
    KubeAPIContext,
    ObjectReference
)

__all__ = (
    'deploy_default_cluster_deployment',
    'deploy_default_secret',
    'deploy_default_infraenv',
    'create_kube_api_client',
    'delete_all_resources',
    'suppress_not_found_error',
    'Platform',
    'InstallStrategy',
    'ClusterDeployment',
    'Secret',
    'Agent',
    'KubeAPIContext',
    'ObjectReference',
    'InfraEnv',
    'Proxy',
    'NMStateConfig',
    'UnexpectedStateError',
)
