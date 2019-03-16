import pytest

from tavern.plugins import load_plugins, get_extra_sessions


class TestLoadPlugins:
    def test_load_plugins_correctly(self, includes):
        """Ensure that we are loading the builtin plugins properly"""
        loaded = load_plugins(includes)

        builtin_names = {"requests", "paho-mqtt"}
        loaded_names = set([l.name for l in loaded])

        assert loaded_names <= builtin_names

    @pytest.mark.parametrize("request_type_name, expected_session_name", [
        ("request", "requests"),
        ("mqtt_publish", "paho-mqtt"),
    ])
    def test_load_expected_sessions(self, includes, request_type_name, expected_session_name):
        test_spec = {
            "stages": [
                {
                    request_type_name: None
                }
            ]
        }

        sessions = get_extra_sessions(test_spec, includes)

        assert expected_session_name in sessions

# class TestGetRequestType:
#     def test_basic_request(self, fake_stage):
#         get_request_type(fake_stage, {}, {})
