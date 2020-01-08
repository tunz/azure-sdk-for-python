# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import map_error

from ... import models


class FileSystemOperations:
    """FileSystemOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    async def create(self, properties=None, request_id=None, timeout=None, *, cls=None, **kwargs):
        """Create FileSystem.

        Create a FileSystem rooted at the specified location. If the FileSystem
        already exists, the operation fails.  This operation does not support
        conditional HTTP requests.

        :param properties: Optional. User-defined properties to be stored with
         the filesystem, in the format of a comma-separated list of name and
         value pairs "n1=v1, n2=v2, ...", where each value is a base64 encoded
         string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties
         not included in the list will be removed.  All properties are removed
         if the header is omitted.  To merge new and existing properties, first
         get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all
         properties.
        :type properties: str
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.file.datalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        if properties is not None:
            header_parameters['x-ms-properties'] = self._serialize.header("properties", properties, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-namespace-enabled': self._deserialize('str', response.headers.get('x-ms-namespace-enabled')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    create.metadata = {'url': '/{filesystem}'}

    async def set_properties(self, properties=None, request_id=None, timeout=None, modified_access_conditions=None, *, cls=None, **kwargs):
        """Set FileSystem Properties.

        Set properties for the FileSystem.  This operation supports conditional
        HTTP requests.  For more information, see [Specifying Conditional
        Headers for Blob Service
        Operations](https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations).

        :param properties: Optional. User-defined properties to be stored with
         the filesystem, in the format of a comma-separated list of name and
         value pairs "n1=v1, n2=v2, ...", where each value is a base64 encoded
         string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties
         not included in the list will be removed.  All properties are removed
         if the header is omitted.  To merge new and existing properties, first
         get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all
         properties.
        :type properties: str
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param modified_access_conditions: Additional parameters for the
         operation
        :type modified_access_conditions:
         ~azure.storage.file.datalake.models.ModifiedAccessConditions
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.file.datalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        if_modified_since = None
        if modified_access_conditions is not None:
            if_modified_since = modified_access_conditions.if_modified_since
        if_unmodified_since = None
        if modified_access_conditions is not None:
            if_unmodified_since = modified_access_conditions.if_unmodified_since

        # Construct URL
        url = self.set_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        if properties is not None:
            header_parameters['x-ms-properties'] = self._serialize.header("properties", properties, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if if_modified_since is not None:
            header_parameters['If-Modified-Since'] = self._serialize.header("if_modified_since", if_modified_since, 'rfc-1123')
        if if_unmodified_since is not None:
            header_parameters['If-Unmodified-Since'] = self._serialize.header("if_unmodified_since", if_unmodified_since, 'rfc-1123')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_properties.metadata = {'url': '/{filesystem}'}

    async def get_properties(self, request_id=None, timeout=None, *, cls=None, **kwargs):
        """Get FileSystem Properties.

        All system and user-defined filesystem properties are specified in the
        response headers.

        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.file.datalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-properties': self._deserialize('str', response.headers.get('x-ms-properties')),
                'x-ms-namespace-enabled': self._deserialize('str', response.headers.get('x-ms-namespace-enabled')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    get_properties.metadata = {'url': '/{filesystem}'}

    async def delete(self, request_id=None, timeout=None, modified_access_conditions=None, *, cls=None, **kwargs):
        """Delete FileSystem.

        Marks the FileSystem for deletion.  When a FileSystem is deleted, a
        FileSystem with the same identifier cannot be created for at least 30
        seconds. While the filesystem is being deleted, attempts to create a
        filesystem with the same identifier will fail with status code 409
        (Conflict), with the service returning additional error information
        indicating that the filesystem is being deleted. All other operations,
        including operations on any files or directories within the filesystem,
        will fail with status code 404 (Not Found) while the filesystem is
        being deleted. This operation supports conditional HTTP requests.  For
        more information, see [Specifying Conditional Headers for Blob Service
        Operations](https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations).

        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param modified_access_conditions: Additional parameters for the
         operation
        :type modified_access_conditions:
         ~azure.storage.file.datalake.models.ModifiedAccessConditions
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.file.datalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        if_modified_since = None
        if modified_access_conditions is not None:
            if_modified_since = modified_access_conditions.if_modified_since
        if_unmodified_since = None
        if modified_access_conditions is not None:
            if_unmodified_since = modified_access_conditions.if_unmodified_since

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if if_modified_since is not None:
            header_parameters['If-Modified-Since'] = self._serialize.header("if_modified_since", if_modified_since, 'rfc-1123')
        if if_unmodified_since is not None:
            header_parameters['If-Unmodified-Since'] = self._serialize.header("if_unmodified_since", if_unmodified_since, 'rfc-1123')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    delete.metadata = {'url': '/{filesystem}'}

    async def list_paths(self, recursive, continuation=None, path=None, max_results=None, upn=None, request_id=None, timeout=None, *, cls=None, **kwargs):
        """List Paths.

        List FileSystem paths and their properties.

        :param recursive: Required
        :type recursive: bool
        :param continuation: Optional.  When deleting a directory, the number
         of paths that are deleted with each invocation is limited.  If the
         number of paths to be deleted exceeds this limit, a continuation token
         is returned in this response header.  When a continuation token is
         returned in the response, it must be specified in a subsequent
         invocation of the delete operation to continue deleting the directory.
        :type continuation: str
        :param path: Optional.  Filters results to paths within the specified
         directory. An error occurs if the directory does not exist.
        :type path: str
        :param max_results: An optional value that specifies the maximum
         number of items to return. If omitted or greater than 5,000, the
         response will include up to 5,000 items.
        :type max_results: int
        :param upn: Optional. Valid only when Hierarchical Namespace is
         enabled for the account. If "true", the user identity values returned
         in the x-ms-owner, x-ms-group, and x-ms-acl response headers will be
         transformed from Azure Active Directory Object IDs to User Principal
         Names.  If "false", the values will be returned as Azure Active
         Directory Object IDs. The default value is false. Note that group and
         application Object IDs are not translated because they do not have
         unique friendly names.
        :type upn: bool
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: PathList or the result of cls(response)
        :rtype: ~azure.storage.file.datalake.models.PathList
        :raises:
         :class:`StorageErrorException<azure.storage.file.datalake.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.list_paths.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if continuation is not None:
            query_parameters['continuation'] = self._serialize.query("continuation", continuation, 'str')
        if path is not None:
            query_parameters['directory'] = self._serialize.query("path", path, 'str')
        query_parameters['recursive'] = self._serialize.query("recursive", recursive, 'bool')
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query("max_results", max_results, 'int', minimum=1)
        if upn is not None:
            query_parameters['upn'] = self._serialize.query("upn", upn, 'bool')
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PathList', response)
            header_dict = {
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-continuation': self._deserialize('str', response.headers.get('x-ms-continuation')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    list_paths.metadata = {'url': '/{filesystem}'}