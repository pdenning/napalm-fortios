"""Tests for getters."""

from napalm_base.test.getters import BaseTestGetters,helpers, wrap_test_cases
from napalm_base.utils.py23_compat import text_type

import pytest


@pytest.mark.usefixtures("set_device_parameters")
class TestGetter(BaseTestGetters):
    """Test get_* methods."""

    @wrap_test_cases
    def test_get_vlans(self, test_case):

        vlan_model = {
            "vlan_id": text_type,
            "name": text_type,
            "description": text_type,
            "role": text_type
        }

        get_vlans = self.device.get_vlans()

        for vlan in get_vlans:
            assert helpers.test_model(vlan_model,vlan)

        return get_vlans

