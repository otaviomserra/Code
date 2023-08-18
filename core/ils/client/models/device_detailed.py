# coding: utf-8

"""
    ILS API Documentation

    Neoception® Intralogistics Suite is a collection of modules for automation in the context of manufacturing.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@neoception.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeviceDetailed(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'organisation_id': 'str',
        'type': 'str',
        'name': 'str',
        'group': 'DeviceGroup',
        'settings': 'dict(str, object)',
        'metadata': 'dict(str, object)',
        'state': 'State',
        'parent': 'Device',
        'children': 'list[Device]',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'organisation_id': 'organisationId',
        'type': 'type',
        'name': 'name',
        'group': 'group',
        'settings': 'settings',
        'metadata': 'metadata',
        'state': 'state',
        'parent': 'parent',
        'children': 'children',
        'create_time': 'createTime',
        'update_time': 'updateTime'
    }

    def __init__(self, id=None, organisation_id=None, type=None, name=None, group=None, settings=None, metadata=None, state=None, parent=None, children=None, create_time=None, update_time=None):  # noqa: E501
        """DeviceDetailed - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organisation_id = None
        self._type = None
        self._name = None
        self._group = None
        self._settings = None
        self._metadata = None
        self._state = None
        self._parent = None
        self._children = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if settings is not None:
            self.settings = settings
        if metadata is not None:
            self.metadata = metadata
        if state is not None:
            self.state = state
        if parent is not None:
            self.parent = parent
        if children is not None:
            self.children = children
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this DeviceDetailed.  # noqa: E501


        :return: The id of this DeviceDetailed.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceDetailed.


        :param id: The id of this DeviceDetailed.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this DeviceDetailed.  # noqa: E501


        :return: The organisation_id of this DeviceDetailed.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this DeviceDetailed.


        :param organisation_id: The organisation_id of this DeviceDetailed.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def type(self):
        """Gets the type of this DeviceDetailed.  # noqa: E501


        :return: The type of this DeviceDetailed.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceDetailed.


        :param type: The type of this DeviceDetailed.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "PF_READER", "PF_LANE_CONTROLLER", "PF_IDENT_CONTROLLER", "SOLUM_E_INK_LABEL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this DeviceDetailed.  # noqa: E501


        :return: The name of this DeviceDetailed.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceDetailed.


        :param name: The name of this DeviceDetailed.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this DeviceDetailed.  # noqa: E501


        :return: The group of this DeviceDetailed.  # noqa: E501
        :rtype: DeviceGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DeviceDetailed.


        :param group: The group of this DeviceDetailed.  # noqa: E501
        :type: DeviceGroup
        """

        self._group = group

    @property
    def settings(self):
        """Gets the settings of this DeviceDetailed.  # noqa: E501

        The setting's of a device  # noqa: E501

        :return: The settings of this DeviceDetailed.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this DeviceDetailed.

        The setting's of a device  # noqa: E501

        :param settings: The settings of this DeviceDetailed.  # noqa: E501
        :type: dict(str, object)
        """

        self._settings = settings

    @property
    def metadata(self):
        """Gets the metadata of this DeviceDetailed.  # noqa: E501

        The metadata of a device  # noqa: E501

        :return: The metadata of this DeviceDetailed.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeviceDetailed.

        The metadata of a device  # noqa: E501

        :param metadata: The metadata of this DeviceDetailed.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

    @property
    def state(self):
        """Gets the state of this DeviceDetailed.  # noqa: E501


        :return: The state of this DeviceDetailed.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeviceDetailed.


        :param state: The state of this DeviceDetailed.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def parent(self):
        """Gets the parent of this DeviceDetailed.  # noqa: E501


        :return: The parent of this DeviceDetailed.  # noqa: E501
        :rtype: Device
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DeviceDetailed.


        :param parent: The parent of this DeviceDetailed.  # noqa: E501
        :type: Device
        """

        self._parent = parent

    @property
    def children(self):
        """Gets the children of this DeviceDetailed.  # noqa: E501


        :return: The children of this DeviceDetailed.  # noqa: E501
        :rtype: list[Device]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DeviceDetailed.


        :param children: The children of this DeviceDetailed.  # noqa: E501
        :type: list[Device]
        """

        self._children = children

    @property
    def create_time(self):
        """Gets the create_time of this DeviceDetailed.  # noqa: E501


        :return: The create_time of this DeviceDetailed.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DeviceDetailed.


        :param create_time: The create_time of this DeviceDetailed.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DeviceDetailed.  # noqa: E501


        :return: The update_time of this DeviceDetailed.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DeviceDetailed.


        :param update_time: The update_time of this DeviceDetailed.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceDetailed, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceDetailed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
