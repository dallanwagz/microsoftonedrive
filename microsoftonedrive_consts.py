# File: microsoftonedrive_consts.py
#
# Copyright (c) 2019-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
MSONEDRIVE_CONFIG_CLIENT_ID = 'client_id'
MSONEDRIVE_CONFIG_CLIENT_SECRET = 'client_secret'
MSONEDRIVE_TOKEN_STRING = 'token'
MSONEDRIVE_ACCESS_TOKEN_STRING = 'access_token'
MSONEDRIVE_REFRESH_TOKEN_STRING = 'refresh_token'
MSONEDRIVE_PHANTOM_SYS_INFO_URL = '/system_info'
MSONEDRIVE_LOGIN_BASE_URL = 'https://login.microsoftonline.com'
MSONEDRIVE_SERVER_TOKEN_URL = '/common/oauth2/token'
MSONEDRIVE_AUTHORIZE_URL = '/common/oauth2/v2.0/authorize?client_id={client_id}&redirect_uri={redirect_uri}' \
    '&response_type={response_type}&scope={scope}&state={state}'
MSONEDRIVE_PHANTOM_ASSET_INFO_URL = '/asset/{asset_id}'
MSONEDRIVE_MSGRAPH_API_BASE_URL = 'https://graph.microsoft.com/v1.0'
MSONEDRIVE_TC_FILE = 'oauth_task.out'
MSONEDRIVE_USER_INFO_ENDPOINT = '/me'
MSONEDRIVE_LIST_DRIVES_ENDPOINT = '/me/drives'
MSONEDRIVE_DELETE_FILE_ID_ENDPOINT = '/me/drive/items/{file_id}'
MSONEDRIVE_DELETE_FILE_ID_DRIVE_ID_ENDPOINT = '/me/drives/{drive_id}/items/{file_id}'
MSONEDRIVE_DELETE_FILE_DRIVE_ID_PATH_ENDPOINT = '/me/drives/{drive_id}/root:/{file_path}'
MSONEDRIVE_DELETE_FILE_PATH_ENDPOINT = '/me/drive/root:/{file_path}'
MSONEDRIVE_LIST_ITEMS_DEFAULT_ENDPOINT = '/me/drive/root/children'
MSONEDRIVE_SMALL_FILE_UPLOAD_IF_DRIVE_ENDPOINT = '/me/drives/{drive_id}/root:/{file_path}:/content'
MSONEDRIVE_SMALL_FILE_UPLOAD_NO_DRIVE_ENDPOINT = '/me/drive/root:/{file_path}:/content'
MSONEDRIVE_CREATE_UPLOAD_SESSION_IF_DRIVE_ENDPOINT = '/me/drives/{drive_id}/root:/{file_path}:/createUploadSession'
MSONEDRIVE_CREATE_UPLOAD_SESSION_NO_DRIVE_ENDPOINT = '/me/drive/root:/{file_path}:/createUploadSession'
MSONEDRIVE_LIST_ITEMS_DRIVE_ID = '/me/drives/{drive_id}/root/children'
MSONEDRIVE_LIST_ITEMS_DRIVE_FOLDER_ID = '/me/drives/{drive_id}/items/{folder_id}/children'
MSONEDRIVE_LIST_ITEMS_DRIVE_FOLDER_PATH = '/me/drives/{drive_id}/root:/{folder_path}:/children'
MSONEDRIVE_LIST_ITEMS_FOLDER_ID = '/me/drive/items/{folder_id}/children'
MSONEDRIVE_LIST_ITEMS_FOLDER_PATH = '/me/drive/root:/{folder_path}:/children'
MSONEDRIVE_DELETE_FOLDER_DRIVE_FOLDER_ID = '/me/drives/{drive_id}/items/{folder_id}'
MSONEDRIVE_DELETE_FOLDER_DRIVE_FOLDER_PATH = '/me/drives/{drive_id}/root:/{folder_path}'
MSONEDRIVE_DELETE_FOLDER_FOLDER_ID = '/me/drive/items/{folder_id}'
MSONEDRIVE_DELETE_FOLDER_FOLDER_PATH = '/me/drive/root:/{folder_path}'
MSONEDRIVE_GET_FILE_DRIVE_FILE_ID = '/me/drives/{drive_id}/items/{file_id}'
MSONEDRIVE_GET_FILE_DRIVE_FILE_PATH = '/me/drives/{drive_id}/root:/{file_path}'
MSONEDRIVE_GET_FILE_FILE_ID = '/me/drive/items/{file_id}'
MSONEDRIVE_GET_FILE_FILE_PATH = '/me/drive/root:/{file_path}'
MSONEDRIVE_PARAM_DRIVE_ID = 'drive_id'
MSONEDRIVE_PARAM_FOLDER_ID = 'folder_id'
MSONEDRIVE_PARAM_FOLDER_PATH = 'folder_path'
MSONEDRIVE_PARAM_FILE_ID = 'file_id'
MSONEDRIVE_PARAM_FILE_PATH = 'file_path'
MSONEDRIVE_PARAM_AUTO_RENAME = 'auto_rename'
MSONEDRIVE_PARAM_FOLDER_NAME = 'folder_name'
MSONEDRIVE_PARAM_VAULT_ID = 'vault_id'
MSONEDRIVE_JSON_ITEM = 'item'
MSONEDRIVE_JSON_UPLOAD_URL = 'uploadUrl'
MSONEDRIVE_PARAM_FILE_PATH = 'file_path'
MSONEDRIVE_JSON_ID = 'id'
MSONEDRIVE_JSON_NAME = 'name'
MSONEDRIVE_JSON_FOLDER = 'folder'
MSONEDRIVE_JSON_RENAME = 'rename'
MSONEDRIVE_JSON_FAIL = 'fail'
MSONEDRIVE_JSON_FILE = 'file'
MSONEDRIVE_JSON_CODE = 'code'
MSONEDRIVE_JSON_SCOPE = 'scope'
MSONEDRIVE_JSON_VALUE = 'value'
MSONEDRIVE_JSON_METADATA = 'metadata'
MSONEDRIVE_JSON_SIZE = 'size'
MSONEDRIVE_JSON_NEXT_LINK = '@odata.nextLink'
MSONEDRIVE_JSON_GRANT_TYPE = 'grant_type'
MSONEDRIVE_JSON_REDIRECT_URI = 'redirect_uri'
MSONEDRIVE_JSON_PARENT_REFERENCE = 'parentReference'
MSONEDRIVE_JSON_PATH = 'path'
MSONEDRIVE_JSON_FOLDER_PATH = 'folderPath'
MSONEDRIVE_JSON_ROOT_SPLIT = 'root:/'
MSONEDRIVE_JSON_ERROR = 'error'
MSONEDRIVE_JSON_CODE = 'code'
MSONEDRIVE_JSON_ERROR_CODES = 'error_codes'
MSONEDRIVE_JSON_MESSAGE = 'message'
MSONEDRIVE_JSON_DRIVE_PATH = 'drivePath'
MSONEDRIVE_JSON_AUTHORIZATION_URL = 'authorization_url'
MSONEDRIVE_JSON_ERROR_DESCRIPTION = 'error_description'
MSONEDRIVE_JSON_NEXT_EXPECTED_RANGES = 'nextExpectedRanges'
MSONEDRIVE_JSON_CONFLICT_BEHAVIOR = '@microsoft.graph.conflictBehavior'
MSONEDRIVE_JSON_PATH_NAME = 'name'
MSONEDRIVE_JSON_PATH_DOWNLOAD_URL = '@microsoft.graph.downloadUrl'
MSONEDRIVE_METHOD_POST = 'post'
MSONEDRIVE_REST_REQUEST_SCOPE = 'files.readwrite.all'
MSONEDRIVE_MAKING_CONNECTION_MSG = 'Testing connectivity. Connecting...'
MSONEDRIVE_REST_URL_NOT_AVAILABLE_MSG = 'Rest URL is not available. Error: {error}'
MSONEDRIVE_TEST_CONNECTIVITY_FAILED_MSG = 'Test Connectivity Failed'
MSONEDRIVE_TEST_CONNECTIVITY_PASSED_MSG = 'Test Connectivity Passed'
MSONEDRIVE_AUTHORIZE_USER_MSG = 'Please authorize user in a separate tab using URL'
MSONEDRIVE_AUTHORIZE_WAIT_TIME = 15
MSONEDRIVE_TC_STATUS_SLEEP = 3
MSONEDRIVE_ERROR_FILE_NOT_EXIST_MSG = 'The requested file does not exist on OneDrive'
MSONEDRIVE_OAUTH_URL_MSG = 'Using OAuth URL:'
MSONEDRIVE_CODE_RECEIVED_MSG = 'Code Received'
MSONEDRIVE_GENERATING_ACCESS_TOKEN_MSG = 'Generating access token'
MSONEDRIVE_TOKEN_NOT_AVAILABLE_MSG = 'Token not available. Please run Test Connectivity first.'
MSONEDRIVE_CURRENT_USER_INFO_MSG = 'Getting info about the current user to verify token'
MSONEDRIVE_GOT_CURRENT_USER_INFO_MSG = 'Got current user info successfully'
MSONEDRIVE_BASE_URL_NOT_FOUND_MSG = 'Phantom Base URL not found in System Settings. ' \
    'Please specify this value in System Settings.'
MSONEDRIVE_LIST_ITEMS_FAILED_MSG = 'List items action failed'
MSONEDRIVE_CREATE_FOLDER_SUCCESSFUL_MSG = 'The folder: {folder_name} is created successfully'
MSONEDRIVE_DELETE_FOLDER_SUCCESSFUL_MSG = 'The folder is deleted successfully'
MSONEDRIVE_MANDATORY_FOLDER_ID_OR_PATH_MSG = 'Either Folder ID or Folder Path is mandatory'
MSONEDRIVE_VAULT_PATH_ABSENT_MSG = 'Vault path not accessible for provided Vault ID'
MSONEDRIVE_VAULT_INFO_ABSENT_MSG = 'Vault info not accessible for provided Vault ID'
MSONEDRIVE_UPLOAD_FILE_SUCCESSFUL_MSG = 'The file is uploaded successfully'
MSONEDRIVE_UPLOAD_FILE_FAILED_MSG = 'Uploading file failed'
MSONEDRIVE_ERROR_READING_VAULT_FILE_MSG = 'Reading file data from vault failed'
MSONEDRIVE_MANDATORY_FILE_ID_OR_PATH_MSG = 'Either File ID or File Path is mandatory'
MSONEDRIVE_NO_DATA_FOUND_MSG = 'File has no content'
MSONEDRIVE_FILE_ALREADY_AVAILABLE = 'File already available in Vault'
MSONEDRIVE_ADD_FILE_TO_VAULT_ERROR = 'Error while adding the file to vault'
MSONEDRIVE_TOKEN_EXPIRED = 'Access token has expired'
MSONEDRIVE_LIST_DRIVE_FAILED_MSG = 'List drive action failed'
MSONEDRIVE_DELETE_FILE_SUCCESS = "File was deleted successfully"
MSONEDRIVE_UNABLE_TO_RETREIVE_VAULT_ITEM_ERR_MSG = "Unable to retrieve vault item details"
DEFAULT_TIMEOUT = 30
