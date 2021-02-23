# -*- coding: utf-8 -*- #
# Copyright 2014 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command for creating target TCP proxies."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import target_proxies_utils
from googlecloudsdk.api_lib.compute import utils
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute.backend_services import (
    flags as backend_service_flags)
from googlecloudsdk.command_lib.compute.target_tcp_proxies import flags


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Create(base.CreateCommand):
  """Create a target TCP proxy."""

  BACKEND_SERVICE_ARG = None
  TARGET_TCP_PROXY_ARG = None
  _support_tcp_in_td = False

  @classmethod
  def Args(cls, parser):
    target_proxies_utils.AddProxyHeaderRelatedCreateArgs(parser)

    cls.BACKEND_SERVICE_ARG = (
        backend_service_flags.BackendServiceArgumentForTargetTcpProxy())
    cls.BACKEND_SERVICE_ARG.AddArgument(parser)
    cls.TARGET_TCP_PROXY_ARG = flags.TargetTcpProxyArgument()
    cls.TARGET_TCP_PROXY_ARG.AddArgument(parser, operation_type='create')

    if cls._support_tcp_in_td:
      flags.AddProxyBind(parser)

    parser.add_argument(
        '--description',
        help='An optional, textual description for the target TCP proxy.')

    parser.display_info.AddCacheUpdater(flags.TargetTcpProxiesCompleter)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())

    backend_service_ref = self.BACKEND_SERVICE_ARG.ResolveAsResource(
        args, holder.resources)

    target_tcp_proxy_ref = self.TARGET_TCP_PROXY_ARG.ResolveAsResource(
        args, holder.resources)

    client = holder.client.apitools_client
    messages = holder.client.messages
    if args.proxy_header:
      proxy_header = messages.TargetTcpProxy.ProxyHeaderValueValuesEnum(
          args.proxy_header)
    else:
      proxy_header = (
          messages.TargetTcpProxy.ProxyHeaderValueValuesEnum.NONE)

    target_tcp_proxy = messages.TargetTcpProxy(
        description=args.description,
        name=target_tcp_proxy_ref.Name(),
        proxyHeader=proxy_header,
        service=backend_service_ref.SelfLink())

    if self._support_tcp_in_td and args.proxy_bind is not None:
      target_tcp_proxy.proxyBind = args.proxy_bind

    request = messages.ComputeTargetTcpProxiesInsertRequest(
        project=target_tcp_proxy_ref.project, targetTcpProxy=target_tcp_proxy)

    errors = []
    resources = holder.client.MakeRequests(
        [(client.targetTcpProxies, 'Insert', request)], errors)

    if errors:
      utils.RaiseToolException(errors)
    return resources


Create.detailed_help = {
    'brief': 'Create a target TCP proxy',
    'DESCRIPTION': """
        *{command}* is used to create target TCP proxies. A target
        TCP proxy is referenced by one or more forwarding rules which
        define which packets the proxy is responsible for routing. The
        target TCP proxy points to a backend service which handle the
        actual requests.
        """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class CreateAlphaBeta(Create):
  """Create a target TCP proxy."""
  _support_tcp_in_td = True
