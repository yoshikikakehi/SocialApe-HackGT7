"""Generated client library for accessapproval version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.accessapproval.v1 import accessapproval_v1_messages as messages


class AccessapprovalV1(base_api.BaseApiClient):
  """Generated client library for service accessapproval version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://accessapproval.googleapis.com/'
  MTLS_BASE_URL = 'https://accessapproval.mtls.googleapis.com/'

  _PACKAGE = 'accessapproval'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'AccessapprovalV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new accessapproval handle."""
    url = url or self.BASE_URL
    super(AccessapprovalV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_approvalRequests = self.FoldersApprovalRequestsService(self)
    self.folders = self.FoldersService(self)
    self.organizations_approvalRequests = self.OrganizationsApprovalRequestsService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_approvalRequests = self.ProjectsApprovalRequestsService(self)
    self.projects = self.ProjectsService(self)

  class FoldersApprovalRequestsService(base_api.BaseApiService):
    """Service class for the folders_approvalRequests resource."""

    _NAME = 'folders_approvalRequests'

    def __init__(self, client):
      super(AccessapprovalV1.FoldersApprovalRequestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Approve(self, request, global_params=None):
      r"""Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalFoldersApprovalRequestsApproveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Approve')
      return self._RunMethod(
          config, request, global_params=global_params)

    Approve.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/approvalRequests/{approvalRequestsId}:approve',
        http_method='POST',
        method_id='accessapproval.folders.approvalRequests.approve',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:approve',
        request_field='approveApprovalRequestMessage',
        request_type_name='AccessapprovalFoldersApprovalRequestsApproveRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Dismiss(self, request, global_params=None):
      r"""Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalFoldersApprovalRequestsDismissRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Dismiss')
      return self._RunMethod(
          config, request, global_params=global_params)

    Dismiss.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/approvalRequests/{approvalRequestsId}:dismiss',
        http_method='POST',
        method_id='accessapproval.folders.approvalRequests.dismiss',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:dismiss',
        request_field='dismissApprovalRequestMessage',
        request_type_name='AccessapprovalFoldersApprovalRequestsDismissRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an approval request. Returns NOT_FOUND if the request does not exist.

      Args:
        request: (AccessapprovalFoldersApprovalRequestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/approvalRequests/{approvalRequestsId}',
        http_method='GET',
        method_id='accessapproval.folders.approvalRequests.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalFoldersApprovalRequestsGetRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

      Args:
        request: (AccessapprovalFoldersApprovalRequestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListApprovalRequestsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/approvalRequests',
        http_method='GET',
        method_id='accessapproval.folders.approvalRequests.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/approvalRequests',
        request_field='',
        request_type_name='AccessapprovalFoldersApprovalRequestsListRequest',
        response_type_name='ListApprovalRequestsResponse',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(AccessapprovalV1.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteAccessApprovalSettings(self, request, global_params=None):
      r"""Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

      Args:
        request: (AccessapprovalFoldersDeleteAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('DeleteAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/accessApprovalSettings',
        http_method='DELETE',
        method_id='accessapproval.folders.deleteAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalFoldersDeleteAccessApprovalSettingsRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def GetAccessApprovalSettings(self, request, global_params=None):
      r"""Gets the settings associated with a project, folder, or organization.

      Args:
        request: (AccessapprovalFoldersGetAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('GetAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/accessApprovalSettings',
        http_method='GET',
        method_id='accessapproval.folders.getAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalFoldersGetAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )

    def UpdateAccessApprovalSettings(self, request, global_params=None):
      r"""Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

      Args:
        request: (AccessapprovalFoldersUpdateAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('UpdateAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/accessApprovalSettings',
        http_method='PATCH',
        method_id='accessapproval.folders.updateAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='accessApprovalSettings',
        request_type_name='AccessapprovalFoldersUpdateAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )

  class OrganizationsApprovalRequestsService(base_api.BaseApiService):
    """Service class for the organizations_approvalRequests resource."""

    _NAME = 'organizations_approvalRequests'

    def __init__(self, client):
      super(AccessapprovalV1.OrganizationsApprovalRequestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Approve(self, request, global_params=None):
      r"""Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalOrganizationsApprovalRequestsApproveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Approve')
      return self._RunMethod(
          config, request, global_params=global_params)

    Approve.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/approvalRequests/{approvalRequestsId}:approve',
        http_method='POST',
        method_id='accessapproval.organizations.approvalRequests.approve',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:approve',
        request_field='approveApprovalRequestMessage',
        request_type_name='AccessapprovalOrganizationsApprovalRequestsApproveRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Dismiss(self, request, global_params=None):
      r"""Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalOrganizationsApprovalRequestsDismissRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Dismiss')
      return self._RunMethod(
          config, request, global_params=global_params)

    Dismiss.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/approvalRequests/{approvalRequestsId}:dismiss',
        http_method='POST',
        method_id='accessapproval.organizations.approvalRequests.dismiss',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:dismiss',
        request_field='dismissApprovalRequestMessage',
        request_type_name='AccessapprovalOrganizationsApprovalRequestsDismissRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an approval request. Returns NOT_FOUND if the request does not exist.

      Args:
        request: (AccessapprovalOrganizationsApprovalRequestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/approvalRequests/{approvalRequestsId}',
        http_method='GET',
        method_id='accessapproval.organizations.approvalRequests.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalOrganizationsApprovalRequestsGetRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

      Args:
        request: (AccessapprovalOrganizationsApprovalRequestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListApprovalRequestsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/approvalRequests',
        http_method='GET',
        method_id='accessapproval.organizations.approvalRequests.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/approvalRequests',
        request_field='',
        request_type_name='AccessapprovalOrganizationsApprovalRequestsListRequest',
        response_type_name='ListApprovalRequestsResponse',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(AccessapprovalV1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteAccessApprovalSettings(self, request, global_params=None):
      r"""Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

      Args:
        request: (AccessapprovalOrganizationsDeleteAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('DeleteAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/accessApprovalSettings',
        http_method='DELETE',
        method_id='accessapproval.organizations.deleteAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalOrganizationsDeleteAccessApprovalSettingsRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def GetAccessApprovalSettings(self, request, global_params=None):
      r"""Gets the settings associated with a project, folder, or organization.

      Args:
        request: (AccessapprovalOrganizationsGetAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('GetAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/accessApprovalSettings',
        http_method='GET',
        method_id='accessapproval.organizations.getAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalOrganizationsGetAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )

    def UpdateAccessApprovalSettings(self, request, global_params=None):
      r"""Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

      Args:
        request: (AccessapprovalOrganizationsUpdateAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('UpdateAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/accessApprovalSettings',
        http_method='PATCH',
        method_id='accessapproval.organizations.updateAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='accessApprovalSettings',
        request_type_name='AccessapprovalOrganizationsUpdateAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )

  class ProjectsApprovalRequestsService(base_api.BaseApiService):
    """Service class for the projects_approvalRequests resource."""

    _NAME = 'projects_approvalRequests'

    def __init__(self, client):
      super(AccessapprovalV1.ProjectsApprovalRequestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Approve(self, request, global_params=None):
      r"""Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalProjectsApprovalRequestsApproveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Approve')
      return self._RunMethod(
          config, request, global_params=global_params)

    Approve.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/approvalRequests/{approvalRequestsId}:approve',
        http_method='POST',
        method_id='accessapproval.projects.approvalRequests.approve',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:approve',
        request_field='approveApprovalRequestMessage',
        request_type_name='AccessapprovalProjectsApprovalRequestsApproveRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Dismiss(self, request, global_params=None):
      r"""Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

      Args:
        request: (AccessapprovalProjectsApprovalRequestsDismissRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Dismiss')
      return self._RunMethod(
          config, request, global_params=global_params)

    Dismiss.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/approvalRequests/{approvalRequestsId}:dismiss',
        http_method='POST',
        method_id='accessapproval.projects.approvalRequests.dismiss',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:dismiss',
        request_field='dismissApprovalRequestMessage',
        request_type_name='AccessapprovalProjectsApprovalRequestsDismissRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an approval request. Returns NOT_FOUND if the request does not exist.

      Args:
        request: (AccessapprovalProjectsApprovalRequestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ApprovalRequest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/approvalRequests/{approvalRequestsId}',
        http_method='GET',
        method_id='accessapproval.projects.approvalRequests.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalProjectsApprovalRequestsGetRequest',
        response_type_name='ApprovalRequest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

      Args:
        request: (AccessapprovalProjectsApprovalRequestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListApprovalRequestsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/approvalRequests',
        http_method='GET',
        method_id='accessapproval.projects.approvalRequests.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/approvalRequests',
        request_field='',
        request_type_name='AccessapprovalProjectsApprovalRequestsListRequest',
        response_type_name='ListApprovalRequestsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(AccessapprovalV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteAccessApprovalSettings(self, request, global_params=None):
      r"""Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

      Args:
        request: (AccessapprovalProjectsDeleteAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('DeleteAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/accessApprovalSettings',
        http_method='DELETE',
        method_id='accessapproval.projects.deleteAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalProjectsDeleteAccessApprovalSettingsRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def GetAccessApprovalSettings(self, request, global_params=None):
      r"""Gets the settings associated with a project, folder, or organization.

      Args:
        request: (AccessapprovalProjectsGetAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('GetAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/accessApprovalSettings',
        http_method='GET',
        method_id='accessapproval.projects.getAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccessapprovalProjectsGetAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )

    def UpdateAccessApprovalSettings(self, request, global_params=None):
      r"""Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

      Args:
        request: (AccessapprovalProjectsUpdateAccessApprovalSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessApprovalSettings) The response message.
      """
      config = self.GetMethodConfig('UpdateAccessApprovalSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateAccessApprovalSettings.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/accessApprovalSettings',
        http_method='PATCH',
        method_id='accessapproval.projects.updateAccessApprovalSettings',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='accessApprovalSettings',
        request_type_name='AccessapprovalProjectsUpdateAccessApprovalSettingsRequest',
        response_type_name='AccessApprovalSettings',
        supports_download=False,
    )